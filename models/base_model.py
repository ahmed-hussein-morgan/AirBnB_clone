#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """A base class for all hbnb models"""
    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
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
            models.storage.new(self)

        # if not kwargs:
        #     from models import storage
        #     self.id = str(uuid.uuid4())
        #     self.created_at = datetime.now()
        #     self.updated_at = datetime.now()
        #     storage.new(self)
        # else:
        #     kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
        #                                              '%Y-%m-%dT%H:%M:%S.%f')
        #     kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
        #                                              '%Y-%m-%dT%H:%M:%S.%f')
        #     del kwargs['__class__']
        #     self.__dict__.update(kwargs)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary
