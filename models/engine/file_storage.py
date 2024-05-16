#!/usr/bin/python3
"""
handle objects and create needed json file:
    retreive, save, add_new, reload 
"""
from models.base_model import BaseModel
import json
class FileStorage:
    """handle the data storage"""
        # path to the json file
    __file_path = "./file.json"

        # store all objects by <class name>.id in this dictionary
        # ex: to store a BaseModel object with id=12121212,
        # the key will be BaseModel.12121212
    __objects = {}

    #returns the dictionary __objects
    def all(self):
        return self.__objects
    
    # add new objects to __objects dictionary
    # paired in key/value
    # key in format <obj class name>.id
    # value is the object
    def new(self, obj):

        #   self.__objects[f'{obj.__class__.__name__}.{obj.id}'] = obj
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    # serializes __objects to the JSON file (path: __file_path)
    #   convert objects in __objects dictionary to Json file
    def save(self):
        # with open(FileStorage.__file_path, "w") as f:
        #     json.dump(FileStorage.__objects, f)
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)


    # deserializes the JSON file to __objects
    #   only if the JSON file (__file_path) exists; otherwise, do nothing.
    #   If the file doesn’t exist, no exception should be raised)
    # convert back Json file in the __file_path to __objects
    def reload(self):
        #pass
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                        self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass
