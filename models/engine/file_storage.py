import json
from os.path import exists
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from models.city import City


class FileStorage:
    """
    Serializes instances to a JSON file and deserializes JSON file to instances
    """

    # Private class attributes
    __file_path = "file.json"
    __objects = {}

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def all(self):
        """Returns the dictionary __objects."""
        return FileStorage.__objects

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        serialized_objects = {key: obj.to_dict() for key,
                              obj in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w', encoding="utf-8") as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """Deserializes the JSON file to __objects(only if the file exists)."""
        if exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding="utf-8") as file:
                try:
                    data = json.load(file)

                    for key, obj_data in data.items():
                        class_name, obj_id = key.split('.')
                        class_ = eval(class_name)
                        obj = class_(**obj_data)
                        FileStorage.__objects[key] = obj
                except Exception:
                    pass
