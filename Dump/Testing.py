import re

my_dict = {}

def parse_code(this):
    fname = re.findall("[^0]+",this)

    
    my_dict["first_name"] = fname[0]
    my_dict["last_name"] = fname[1]
    my_dict["id"] = fname[2]
    return(my_dict)

assert parse_code("John000Doe000123"),{'first_name': 'John', 'last_name': 'Doe', 'id': '123'}
assert parse_code("michael0smith004331"),{"first_name": "michael","last_name": "smith","id": "4331"}
assert parse_code("Thomas00LEE0000043"),{"first_name": "Thomas","last_name": "LEE","id": "43"}