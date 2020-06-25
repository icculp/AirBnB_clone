#!/usr/bin/python3
"""
    Base Model
    HolbertonBnB
"""
import cmd, uuid, datetime


class BaseModel(cmd.Cmd):
    """ BaseModel class for command interpreter """

    def __init__(self):
        """ constructor for BaseModel """
        self.id = uuid.uuid4()
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """ string representation of our badass command interpreter """
        s = "[{}] ({}) {}".format(str(type(self).__name__), self.id, self.__dict__)
        return s

    def save(self):
        """ saves up in this motherfucker """
        self.updated_at = datetime.datetime
        
    def to_dict(self):
        """ two dicks """
        '''self.__dict__.update({"__class__") = str(type(self).__name__)'''
        self.__dict__['__class__'] = str(type(self).__name__)
        self.__dict__['created_at'] = self.created_at.now().isoformat()
        self.__dict__['updated_at'] = self.updated_at.now().isoformat()
        return self.__dict__
