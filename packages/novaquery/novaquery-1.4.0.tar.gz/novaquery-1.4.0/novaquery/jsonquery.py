import json
from cache import CacheFile
import re

class JSONQuery:
    @staticmethod
    def from_string(obj: str) -> "JSONQuery":
        """Creates a JSONQuery object from a string

        Args:
            obj (str): the string to parse

        Returns:
            JSONQuery: the object created or None if the string is not a valid JSON

        """
        try:
            return JSONQuery(json.loads(obj))
        except:
            return None

    @staticmethod
    def from_file(filename: str) -> "JSONQuery":
        """Builds the object from the content of a file

        Args:
            filename (str): a file that contains a JSON object

        Returns:
            JSONQuery: the JSOnQuery object created or None if the file cannot be loaded
        """
        try:
            return JSONQuery.from_string(open(filename, "r").read())
        except:
            return None


    def __init__(self, obj: dict) -> None:
        """Builds the object

        Args:
            obj (dict): the JSON object to use
        """
        self._obj = obj

    @staticmethod
    def find_key(obj: dict, key: str) -> dict:
        """Queries the object for the value of a key

        Args:
            key (str): the key to query

        Returns:
            dict: the value of the key or None if the key does not exist
        """
        keys = key.split(".")
        current = obj

        r = re.compile(r"^\[(?P<index>[0-9]*)\](\[|$)")

        for key in keys:
            ppos = key.find('[')
            if (ppos >= 0):
                indexes = key[ppos:]
                key = key[:ppos]

                # If the current object has not the key, return None
                if key not in current:
                    return None
                current = current[key]

                # We'll enable [0][1][2] style queries
                while indexes != "":

                    # If this object is not a list, return None
                    if not isinstance(current, list):
                        return None

                    # Get the index and advance the indexes, but if one of them is not valid, return None
                    m = r.search(indexes)
                    if m is None:
                        return None
                    index = m.group("index")
                    try:
                        index = int(index)
                        current = current[index]
                    except:
                        return None

                    # Get to the next [] construction
                    indexes = indexes[m.end():]
            else:
                # If it is a dict, we are on the way; otherwise it is a list and we are not querying it as a list
                if isinstance(current, dict):
                    if key in current:
                        current = current[key]
                    else:
                        return None
                else:
                    return None

        return current

    @staticmethod
    def query_key(obj: dict, _key: str) -> dict:
        if _key == "":
            return obj

        keys = _key.split(".")

        r = re.compile(r"^\[(?P<index>[0-9]*)\](\[|$)")

        keys_with_square_brackets = []
        # for key in keys:
        key = keys[0]
        square_pos = key.find('[')
        if square_pos > 0:
            square_part = key[square_pos:]
            key = key[:square_pos]
            # keys_with_square_brackets.append(key[:square_pos])
            while square_part != "":
                m = r.search(square_part)
                if m is None:
                    raise Exception(f"Invalid square bracket syntax: {_key}")
                keys_with_square_brackets.append(square_part[:m.end()])
                square_part = square_part[m.end():]

        if isinstance(obj, dict):
            if key in obj:
                return { key: __class__.query_key(obj[key], ".".join(keys_with_square_brackets + keys[1:])) }
        elif isinstance(obj, list):
            m = r.match(key)
            if m is None:
                return None
            index = m.group("index")
            if index == "":
                return [ __class__.query_key(obj[i], ".".join(keys_with_square_brackets + keys[1:])) for i in range(len(obj)) ]
            else:
                try:
                    index = int(index)
                    return __class__.query_key(obj[index], ".".join(keys_with_square_brackets + keys[1:]))
                except:
                    return None
        else:
            return None

    def key(self, key: str) -> dict:
        """Queries the object for the value of a key

        Args:
            key (str): the key to query

        Returns:
            dict: the value of the key or None if the key does not exist
        """
        return __class__.find_key(self._obj, key)

    def __str__(self) -> str:
        """Returns the string representation of the object

        Returns:
            str: the string representation of the object
        """
        return json.dumps(self._obj, indent=4)

    def query(self, key: str) -> dict:
        """Queries the object for the value of a key

        Args:
            key (str): the key to query

        Returns:
            dict: the value of the key or None if the key does not exist
        """

        return __class__.query_key(self._obj, key)


def matches(obj: dict, _key: str, value, cmp: str = "=") -> bool:
    """Checks if the value of a key matches a certain value"""

    if _key == "":
        # TODO: implement other types of comparison
        if value is None:
            return True
        else:
            return obj == value

    keys = _key.split(".")

# FALTA HACER algo tipo 
#   - "select * from servers[] where links[0].href=..."
#       que devuelva el contenido completo de cada "server" que hace match con la query
#   - "select links[0].href from servers[] where links[0].href=... " 
#       que devuelva el contenido del primer link de cada "server" que hace match con la query
#   - luego soportar otras operaciones, como >, <, >=, <=, !=, =, like, etc.

# ** Existe algo llamado jsonpath-ng: https://github.com/h2non/jsonpath-ng

servers = {
    'servers': [
        {
            "links": [
                {
                    "href": "https://horsemen.i3m.upv.es:8774/v2.1/servers/65a247f7-41d4-480a-a343-baa72f25cce3",
                    "rel": "self"
                },
                {
                    "href": "https://horsemen.i3m.upv.es:8774/servers/65a247f7-41d4-480a-a343-baa72f25cce3",
                    "rel": "bookmark"
                }
            ]
        },
        {
            "links": [
                {
                    "href": "https://horsemen.i3m.upv.es:8774/v2.1/servers/d6bc1688-55de-48f1-93cd-4e14a6b01528",
                    "rel": "self"
                },
                {
                    "href": "https://horsemen.i3m.upv.es:8774/servers/d6bc1688-55de-48f1-93cd-4e14a6b01528",
                    "rel": "bookmark"
                }
            ]
        },
    ]
}

# j=JSONQuery(servers)
# print(json.dumps(j.query("servers[].links[0].href")))
# import jsonpath_ng as js
# j = js.parse("servers[*].links[0].href")
# print(j.find(servers)[1].value)




def parse(_key: str):
    keys = _key.split(".")


