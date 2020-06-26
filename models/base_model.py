#!/usr/bin/python3
"""
    Base Model
    HolbertonBnB
"""
import cmd
import uuid
import datetime
from models import storage


class BaseModel(cmd.Cmd):
    """ BaseModel class for command interpreter """

    def __init__(self, *args, **kwargs):
        """ constructor for BaseModel """
        if kwargs:
            for item in list(kwargs.keys()):
                if item == 'created_at' or item == 'updated_at':
                    self.__dict__[item] = datetime.datetime.strptime(
                        kwargs[item], '%Y-%m-%dT%H:%M:%S.%f')
                else:
                    self.__dict__[item] = kwargs[item]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            storage.new(self.__dict__)

    def __str__(self):
        """ string representation of our badass command interpreter """
        s = "[{}] ({}) {}".format(str(
            type(self).__name__), self.id, self.__dict__)
        return s

    def save(self):
        """ saves up in this motherfucker """
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        """ two dicks """
        '''self.__dict__.update({"__class__") = str(type(self).__name__)'''
        self.__dict__['__class__'] = str(type(self).__name__)
        self.__dict__['created_at'] = self.created_at.now().isoformat()
        self.__dict__['updated_at'] = self.updated_at.now().isoformat()
        return self.__dict__
