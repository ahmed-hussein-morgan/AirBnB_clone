#!/usr/bin/python3
"""the file storage module
to handdle the data storage of the project
"""
import json
import os.path
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.review import Review

classes = {
    "BaseModel": BaseModel,
    "User": User,
    "City": City,
    "Place": Place,
    "Amenity": Amenity,
    "Review": Review,
    "State": State
    }


class FileStorage:
    """handle the data storage"""
    def __init__(self) -> None:
        self.__file_path = "./file.json"
        self.__objects = {}

    def all(self):
        """returns the dictionary of all created objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key
        in formate:
        <obj class name>.id
        """
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        data_dict = {}
        data_str = ""

        for key, value in self.__objects.items():
            data_dict[key] = value.to_dict()

        data_str = json.dumps(data_dict)

        with open(self.__file_path, 'w') as file:
            file.write(data_str)

    def reload(self):
        """deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists;
        otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised)
        """

        dict1 = {}
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r") as f:
                dict1 = json.loads(f.read())

            for key, obj_dict in dict1.items():
                cls = globals()[obj_dict['__class__']]
                self.__objects[key] = cls(**obj_dict)
