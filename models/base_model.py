#!/usr/bin/python3
"""
the Base model for all inhereted models
contain all common attributes and methods between all models
"""
import uuid
from datetime import datetime
import models

class BaseModel:
    """the main / parent class"""
    def __init__(self, *args, **kwargs) -> None:
        """ the initialization method """

        if kwargs:
            for key in list(kwargs.keys()):
                if key == "__class__":
                    del kwargs[key]
            
            if "created_at" in kwargs:
                kwargs["created_at"] = datetime.strptime(kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
            if "updated_at" in kwargs:
                kwargs["updated_at"] = datetime.strptime(kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")

            self.__dict__.update(kwargs)
        
        else:
            # assign id when instance created
            self.id = str(uuid.uuid4())

            # assign with the current datetime when an instance is created
            self.created_at = datetime.now()

            # assign with the current datetime when an instance is created
            # and it will be updated every time you change your object
            self.updated_at = datetime.now()

    # The __str__() method returns a human-readable string representation\
    # of an object
    def __str__(self) -> str:
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'
    
    # updates the public instance attribute updated_at with the current datetime
    def save(self):
        # models.storage.save()
        # if f'{self.__class__.__name__}.{self.id}' not in models.storage.__objects: ##need to update
        #     models.storage.new()
        self.updated_at = datetime.now()
        models.storage.save()

    # returns a dictionary containing all keys/values of __dict__ of the instance
    #   change the format of create_at and update_at to iso format
    #   add the class name as a value to __class__ inside the dict
    def to_dict(self):
        self.created_at = datetime.isoformat(self.created_at)
        self.updated_at = datetime.isoformat(self.updated_at)
        self.__dict__.__setitem__('__class__', self.__class__.__name__)
        return self.__dict__