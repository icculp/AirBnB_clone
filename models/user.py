#!/usr/bin/python3
"""
    User Model
    HolbertonBnB
"""
from models.base_model import BaseModel


class User(BaseModel):
    """ User class for HBNB """

    def __init__(self, *args, **kwargs):
        """ constructor for User """
        '''from models import storage'''
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
        super().__init__(**kwargs)
