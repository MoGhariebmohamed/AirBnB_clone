import json
from os.path import exists

class FileStorage:
    """Serializes instances to a JSON file and deserializes JSON file to instances."""

    # Private class attributes
    __file_path = "file.json"
    __objects = {}
    
def all(self):
    """Returns the dictionary __objects."""
    return self.__objects

def new(self, obj):
    """Sets in __objects the obj with key <obj class name>.id."""
    key = "{}.{}".format(obj.__class__.__name__, obj.id)
    self.__objects[key] = obj

def save(self):
    """Serializes __objects to the JSON file (path: __file_path)."""
    serialized_objects = {key: obj.to_dict() for key, obj in self.__objects.items()}
    with open(self.__file_path, 'w') as file:
        json.dump(serialized_objects, file)

def reload(self):
    """Deserializes the JSON file to __objects (only if the file exists)."""
    if exists(self.__file_path):
        with open(self.__file_path, 'r') as file:
            data = json.load(file)
            for key, obj_data in data.items():
                class_name, obj_id = key.split('.')
                class_ = globals()[class_name]
                obj = class_(**obj_data)
                self.__objects[key] = obj