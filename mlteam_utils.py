# The following part is just for seeing the output in a formatted way.
def to_dict(object): 
    if type(object) == list:
         for i, item in enumerate(object):
            object[i] = to_dict(item)
    if type(object) == dict:
        for key, value in object.items():
            object[key] = to_dict(value)
    if hasattr(object, "__dict__"): return to_dict(object.__dict__)
    return object

def print_object(object):
    import json
    print(json.dumps(to_dict(object), indent=4))