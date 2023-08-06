from selector import Field, List

f = Field("servers") + Field("in")

class Token:
    T_NOTOKEN = "No token"
    T_IDENTIFIER = "Identifier"
    T_IDENTIFIER_SPECIAL = "Special identifier"
    T_DOT = "."
    T_DOT_DOT = ".."
    T_ROOT = "$"
    T_INTEGER = "Integer"
    T_FLOAT = "Float"
    T_STRING = "String"
    T_SQ_OPEN = "["
    T_SQ_CLOSE = "]"
    T_RANGE_SEPARATOR = ":"
    T_SEPARATOR = "Separator"
    T_EOF = "EOF"

    def __init__(self, token = T_NOTOKEN, data = None):
        self._token = token
        self._data = data
        self.position = None
    @property
    def token(self):
        return self._token
    @property
    def data(self):
        return self._data
    def __str__(self):
        if isinstance(self._data, str):
            retval = f"{self._token} ({self._data[:32]})"
        else:
            retval = f"{self._token} ({self._data})"
        if self.position is not None:
            retval += f" at {self.position}"
        return retval
    def __ne__(self, other):
        return not self.__eq__(other)
    def __eq__(self, other):
        if isinstance(other, Token):
            return self._token == other.token and self._data == other.data
        return self._token == other

class Parser:
    def __init__(self) -> None:
        self._c = None
        self._n = None
        self._pos = None
        self._buffer = None
        self._token = Token()
        self._eat_spaces = []

    def push_eat_spaces(self, eat: bool) -> bool:
        """Pushes a state to eat spaces in the stack. If the top of the stack is True, when searching for a token,
             the spaces are automatically skipped. If false, they are not skipped and the token T_SEPARATOR will
             appear whenever a set of spaces is found.

        Args:
            eat (bool): automatically skip spaces

        Returns:
            bool: the previous state
        """
        retval = self.eat_spaces
        self._eat_spaces.append(eat)
        return retval

    def pop_eat_spaces(self) -> bool:
        """Pops the top of the stack of eat spaces and returns it
        
            (*) see description of push_eat_spaces for more information

        Returns:
            bool: the previous state
        """
        if len(self._eat_spaces) > 0:
            return self._eat_spaces.pop()
        return True
    @property
    def eat_spaces(self) -> bool:
        """Returns the state of automatically eating the spaces. If no state has been set, the default behavior is
            to eat spaces.

           If eat_spaces is true, when searching for a token, the spaces are automatically skipped. If false, they are
             not skipped and the token T_SEPARATOR will appear whenever a set of spaces is found.

        Returns:
            bool: the state of automatically eating the spaces
        """
        if len(self._eat_spaces) == 0:
            return True
        return self._eat_spaces[-1]
        
    def parse(self, s: str) -> None:
        self._buffer = s
        self._pos = 0
        self._n = self._buffer[0]
        self._c = None
        self._next_c()
        s = self._parse_expression()
        if self._token != Token.T_EOF:
            raise Exception(f"Unexpected token: {self.token}")
        print(s)

    def _is_keyword(self, token):
        if token == Token.T_IDENTIFIER:
            if token.data in ["true", "false", "null"]:
                return True
        return False

    def _parse_expression(self):
        # We won't let the parser eat spaces, because we do not want to allow spaces in the expression (i.e. "field1.field2[]" is
        # valid, but "field1 . field2[]" is not)
        self.push_eat_spaces(False)

        self.next_token()
        if self.token == Token.T_ROOT:
            # Just ignore the root as it can be ommited
            self.next_token()
            s = self._parse_expression_rest()
        elif self.token == Token.T_IDENTIFIER and not self._is_keyword(self.token):
            s = self.token.data
            self.next_token()
            s += self._parse_expression_rest()
        else:
            raise Exception("Invalid expression")

        # Recover the previous state
        self.pop_eat_spaces()

        # This is because the spaces were allowed in the expression, so we can find separators at the end, before
        #   the end of the expression
        if self.token == Token.T_SEPARATOR:
            self.next_token()
        return s

    def _parse_expression_rest(self):
        s = ""
        if self.token == Token.T_DOT:
            self.next_token()
            if self.token != Token.T_IDENTIFIER:
                raise Exception(f"Identifier expected: {self}")
            s = f".{self.token.data}" 
            self.next_token()
            s+= self._parse_expression_rest()
        elif self.token == Token.T_SQ_OPEN:
            s = self._parse_square_bracket() + self._parse_expression_rest()
        return s

    def _parse_range_slice(self):
        if not self.token in [Token.T_INTEGER, Token.T_RANGE_SEPARATOR, Token.T_SQ_CLOSE]:
            raise Exception("Invalid range slice")
        start = None
        end = None
        slice = False
        if self.token == Token.T_INTEGER:
            start = self.token.data
            self.next_token()
        if self.token == Token.T_RANGE_SEPARATOR:
            slice = True
            self.next_token()
            if self.token == Token.T_INTEGER:
                end = self.token.data
                self.next_token()
        s = ""
        if start is not None:
            s += f"{start}"
        if slice:
            s += ":"
        if end is not None:
            s += f"{end}"
        return f"[{s}]"

    def _parse_square_bracket(self):
        """Parses the square bracket expression: [start:end], or ['identifier']

        Raises:
            Exception: if some of the mandatory constructions are not found

        Returns:
            _type_: _description_
        """

        # Make sure that the square bracket is opened        
        if self.token != Token.T_SQ_OPEN:
            raise Exception("Invalid square bracket")

        # We will let the parser to eat spaces because inside the brackets, we want to allow separators (e.g [1:2] is valid, but [ 1: 2]
        #  is also valid)
        self.push_eat_spaces(True)

        # Start with the expression
        self.next_token()
        if self.token == Token.T_STRING:
            s = f"[{self.token.data}]"
        elif self.token in [Token.T_INTEGER, Token.T_RANGE_SEPARATOR, Token.T_SQ_CLOSE]:
            s = self._parse_range_slice()
        else:
            raise Exception("Invalid expression")

        # Make sure that the square bracket is closed
        if self.token != Token.T_SQ_CLOSE:
            raise Exception(f"Invalid square bracket: {self.token}")

        # End the expression and recover the state of eating spaces
        self.next_token()
        self.pop_eat_spaces()
        return s

    def _next_c(self) -> None:
        """Gets the next character from the buffer"""
        self._pos += 1
        self._c = self._n
        if self._pos < len(self._buffer):
            self._n = self._buffer[self._pos]
        else:
            self._n = None

    def __str__(self):
        """Returns a string representation of the parser"""
        return f"at pos {self._pos} (\"{self._c}\")"

    @property
    def token(self) -> "Token":
        """This is a property that represents the current token of the parser.

        Returns:
            Token: The token that is currently being parsed
        """
        return self._token

    def next_token(self) -> "Token":
        """Gets to the next token in the buffer.

        Returns:
            Token: The next token to parse (it is the same than self.token)
        """

        # If no character is available, we are at the end of the buffer
        if self._c is None:
            self._token = Token(Token.T_EOF)
            return self._token

        # Skip spaces (if enabled)
        self._skip_whitespaces()

        token = Token()
        beginning = self._pos

        # First we check the "single char tokens"
        if self._c == "$":
            token = Token(Token.T_ROOT)
        elif self._c == "[":
            token = Token(Token.T_SQ_OPEN)
        elif self._c == "]":
            token = Token(Token.T_SQ_CLOSE)
        elif self._c == ".":
            if self._n == ".":
                self._next_c()
                token = Token(Token.T_DOT_DOT)
            else:
                token = Token(Token.T_DOT)
        elif self._c == ":":
            token = Token(Token.T_RANGE_SEPARATOR)

        if token != Token.T_NOTOKEN:
            # Skip the character of the single-char token
            self._next_c()
        else:
            # Now we check the "multi char tokens", starting from the space (that will appear as a token if eating spaces
            #   is not enabled)
            if self._c.isspace():
                s = ""
                while self._c is not None and self._c.isspace():
                    s += self._c
                    self._next_c()
                token = Token(Token.T_SEPARATOR, s)
            elif self._c == "'":
                token = self._token_quoted_string()
            elif self._c.isdigit():
                token = self._token_number()
            elif self._c.isalpha() or self._c == "_":
                token = self._token_identifier()

        # If we have not recognized the token, we will raise an exception
        if token == Token.T_NOTOKEN:
            raise Exception(f"Invalid character: {self._c}")

        # Store the token and return
        token.position = beginning
        self._token = token
        return token

    def _skip_whitespaces(self):
        """Skips the whitespaces in the buffer, if enabled
            (*) see self.eat_spaces for more information
        """
        if self.eat_spaces:
            while self._c is not None and self._c.isspace():
                self._next_c()

    def _token_identifier(self) -> "Token":
        """Parses the identifier token

        Raises:
            Exception: If the identifier is not valid 
                (*) this should not happen because it is a private method, and we'll call the function if appropriate
                
        Returns:
            Token: the token that was parsed
        """

        # Make sure that the first character is a letter
        if not self._c.isalpha():
            raise Exception("Invalid identifier")

        # Store the identifier
        s = ""
        while self._c is not None and (self._c.isalpha() or self._c.isdigit() or self._c == '_'):
            s += self._c
            self._next_c()

        # Return the identifier
        return Token(Token.T_IDENTIFIER, s)

    def _token_quoted_string(self) -> "Token":
        """Parses the quoted string token. If the string starts with ", it is expected to end with ". If it starts with
            ' it is expected to end with '. The string accepts escaped characters.

        Raises:
            Exception: If there was no string to parse

        Returns:
            Token: the token that was parsed
        """

        # Make sure that the first character is a quote
        if self._c not in [ "'", '"']:
            raise Exception("Quote expected")

        # Get the quote, but do not store it
        quote = self._c
        self._next_c()

        # Get the content of the string
        s = ""
        while self._c is not None and self._c != quote:
            s += self._c

            # Skip escaped chars
            if self._c == "\\":
                self._next_c()
                s += self._c
            self._next_c()
        
        # Make sure that the string ends with the same quote
        if self._c != quote:
            raise Exception("Closing quote expected")
        
        # Skip the closing quote and return
        self._next_c()
        return Token(Token.T_STRING, s)

    def _token_number(self) -> "Token":
        """Parses the number token. It can be an integer or a float point number in the format 1.1e+5

        Raises:
            Exception: If some of the mandatory parts of the number are missing

        Returns:
            Token: the token that was parsed (either T_INTEGER or T_FLOAT)
        """

        # Make sure that the first character is a digit
        if not self._c.isdigit():
            raise Exception("Number expected")

        # Store the number while it is a number
        s = ""
        while self._c is not None and self._c.isdigit():
            s += self._c
            self._next_c()
        
        # If there is no dot, we have an integer
        if self._c != ".":
            return Token(Token.T_INTEGER, int(s))

        # Otherwise, we have a float point number... so continue parsing
        s += self._c
        self._next_c()

        # Make sure that the next character is a digit to avoid accepting numbers like 1.e+5
        if not self._c.isdigit():
            raise Exception("Number expected")

        # Store the right part of the number, while it is a digit
        while self._c is not None and self._c.isdigit():
            s += self._c
            self._next_c()
        
        # If we have an exponent, store it
        if self._c in ["e", "E"]:
            s += self._c
            self._next_c()

            # Store the sign of the exponent (if provided)
            if self._c in ["+", "-"]:
                s += self._c
                self._next_c()

            # Make sure that there is a digit after the exponent, to avoid accepting numbers like 1e+
            if not self._c.isdigit():
                raise Exception("Number expected")

            # Store the exponent, while it is a digit
            while self._c is not None and self._c.isdigit():
                s += self._c
                self._next_c()
            
        # Return the floating number token
        return Token(Token.T_FLOAT, float(s))

p = Parser()
p.parse("server[ 1: ].name ")
print(p)

