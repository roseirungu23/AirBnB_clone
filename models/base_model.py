#!/usr/bin/python3
"""Defines class BaseModel"""

import uuid
from datetime import datetime


class BaseModel:
    """Represents class BaseModel"""
    def __init__(self, *args, **kwargs):
        """Initializes class BaseModel"""
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key in ['created_at', 'updated_at']:
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def save(self):
        """Updates the public instance attribute updated_at with
            the current datetime and saves it"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of
            __dict__ of the instance"""
        new_dict = dict(self.__dict__)
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.__dict__['created_at'].isoformat()
        new_dict['updated_at'] = self.__dict__['updated_at'].isoformat()
        return new_dict

    def __str__(self):
        """Prints: [<class name>] (<self.id>) <self.__dict__>"""
        return "[{}] ({}) {}".format(self.__class__.__name,
                                     self.id, self.__dict__)
