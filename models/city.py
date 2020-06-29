#!/usr/bin/python3
"""
    City Model
    HolbertonBnB
"""
from models.base_model import BaseModel


class City(BaseModel):
    """ User class for HBNB """

    def __init__(self, *args, **kwargs):
        """ constructor for User """
        '''from models import storage'''
        self.state_id = ""
        self.name = ""
        super().__init__(**kwargs)
