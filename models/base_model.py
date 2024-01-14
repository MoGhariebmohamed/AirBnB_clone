#!/usr/bin/python3
import json
import uuid
from datetime import datetime
""" class base model for the project """


class BaseModel:
    """defines all common attributes/methods for other classes"""

    def __init__(self):
        """
        string - assign with an uuid when an instance is created
            args:
                generate unique
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def save(self):
        """updates the public instance attribute"""
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        """returns a dictionary containing all keys/values"""
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = self.__class__.__name__
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary

    def __str__(self):
        """to print the instance as a string representation"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                       self.id, self.__dict__)
