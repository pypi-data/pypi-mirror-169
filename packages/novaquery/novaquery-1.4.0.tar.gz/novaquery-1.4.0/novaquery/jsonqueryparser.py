import json
import sys
"""
La idea es intentar hacer una especie de compilador "similar" a jsonpath-ng, porque lo que queremos es hacer queries tipo SQL en objetos JSON, pero permitiendo
  reconstruir los objetos.

  Ejemplo:

    Teniendo algo como

    servers = [
        {
            "flavor": {
                "ephemeral": 0,
                "ram": 131072,
                "original_name": "oversized",
                "vcpus": 4,
                "extra_specs": [],
                "swap": 0,
                "disk": 80
            },
            "id": "74688b15-4d78-4ab3-bd20-e0fbafdd68ab",
            "security_groups": [
                {
                    "name": "default"
                }
            ]
        },
        {
            "flavor": {
                "ephemeral": 40,
                "ram": 16000,
                "original_name": "Large",
                "vcpus": 4,
                "extra_specs": [],
                "swap": 8000,
                "disk": 14
            },
            "id": "538f6145-7d28-44ba-b554-58a98a51bead",
            "security_groups": [
                {
                    "name": "im-6706e75c-fb96-11ec-94ce-7e73a0e86b1d-public"
                },
                {
                    "name": "im-6706e75c-fb96-11ec-94ce-7e73a0e86b1d"
                },
            ]
        }
    ]

    select id, security_groups from servers[] where flavor[].ephemeral > 0

    obtendría:
    [
        {
            "id": "538f6145-7d28-44ba-b554-58a98a51bead",
            "security_groups": [
                {
                    "name": "im-6706e75c-fb96-11ec-94ce-7e73a0e86b1d-public"
                },
                {
                    "name": "im-6706e75c-fb96-11ec-94ce-7e73a0e86b1d"
                },
            ]
        }
    ]

    Estas cosas se pueden complicar mas, añadiendo "ANDs" y "ORs" en las queries, por ejemplo... o multiples campos en la query, etc. También se le puede añadir
      cosas como slicing de los resultados, etc. pero de momento vamos a hacer la versión mas simple.

    Voy a intentar incorporar cosas de jsonpath, como el uso de .., slices, etc., dando una interpretación intuitiva dentro del contexto SQL.

    Por ejemplo, en el "where" tendría sentido el "..", pero en el "select" habría que interpretar si se quiere guardar "toda la ruta" o solo la subruta. En cualquier
      caso, eso se podría complementar con un "AS" de SQL pero de momento no se va a implementar
"""

servers = {
    "servers": 
    {
        "in":
        [
            {
                "flavor": {
                    "ephemeral": 0,
                    "ram": 131072,
                    "original_name": "oversized",
                    "vcpus": 4,
                    "extra_specs": [],
                    "swap": 0,
                    "disk": 80
                },
                "id": "74688b15-4d78-4ab3-bd20-e0fbafdd68ab",
                "security_groups": [
                    {
                        "name": "default"
                    }
                ]
            },
            {
                "flavor": {
                    "ephemeral": 10,
                    "ram": 131072,
                    "original_name": "oversized",
                    "vcpus": 4,
                    "extra_specs": [],
                    "swap": 0,
                    "disk": 80
                },
                "id": "74688b15-4d78-4ab3-bd20-e0fbafdd68ab",
                "security_groups": [
                    {
                        "name": "default"
                    }
                ]
            },            {
                "flavor": {
                    "ephemeral": 40,
                    "ram": 16000,
                    "original_name": "Large",
                    "vcpus": 4,
                    "extra_specs": [],
                    "swap": 8000,
                    "disk": 14
                },
                "id": "538f6145-7d28-44ba-b554-58a98a51bead",
                "security_groups": [
                    {
                        "name": "im-6706e75c-fb96-11ec-94ce-7e73a0e86b1d-public"
                    },
                    {
                        "name": "im-6706e75c-fb96-11ec-94ce-7e73a0e86b1d"
                    },
                ]
            }
        ]
    }
}




def merge(obj1, *objs):
    for obj2 in objs:
        if (type(obj1) != type(obj2)):
            raise TypeError("Cannot merge objects of different types")
        if isinstance(obj2, list):
            obj1 = obj1 + [ merge({}, x) for x in obj2 ]
            continue
        if isinstance(obj2, dict):
            for k, v in obj2.items():
                if k not in obj1:
                    if isinstance(v, dict):
                        obj1[k] = {}
                    elif isinstance(v, list):
                        obj1[k] = []
                if isinstance(v, dict):
                    obj1[k] = merge(obj1[k], v)
                elif isinstance(v, list):
                    obj1[k] = merge(obj1[k], v)
                else:
                    obj1[k] = v
            continue
        raise TypeError("Cannot merge simple objects")
    return obj1


def select(from_, where_):
    pass

if __name__ == "__main__":

    from_ = Field('servers') + Field('in')
    from_ = from_.get(servers)
    print(json.dumps(from_, indent=4))

    def where(obj, filter_):
        if not isinstance(obj, list):
            return []
        return filter(lambda x: filter_.matches(x, 10, operation=">="), obj)

    where_ = Field('flavor') + Field('ephemeral')

    print(json.dumps(merge([], list(where(from_, where_))), indent = 4))


    #servers = servers['servers']['in']
    #print(servers)
    #f = List() + Field('flavor') + Field('ephemeral')
    #print(list(f.explode(servers)))

    sys.exit()

    filter_ = Field("servers") + Field("in") + List() + Field("flavor")
    print(filter_)
    print(filter_.get(servers))
    filtered = list(filter_.explode(servers))
    print(filtered)
    selector = Field("servers") + Field("in") + List() + Field("flavor") + Field("ram")
    print(merge({}, *list(filter(lambda x: selector.matches(x, 16000, operation=">"), filtered))))
    # print(json.dumps(merge({}, *list(filter.explode(servers))), indent=4))

    # Selector_Field("servers"), Selector_Field("in"), Selector_Index()


    # class Parser:
    #     def __init__(self):
    #         self._c = None
    #         self._pos = 0

    #     """
    #     <identifier> ::= <letter> { <letter> | <digit> }*
    #     <array> ::= \[ <expression> | <numeric expression> \]
    #     <numeric expression> ::= [ <number> | ] [ : [ <number> | ] ]
    #     <expression> ::= ' .* '
    #     """
    #     def next(self):
    #         pass


    # def select(values_, from_, where_):
    #     pass
