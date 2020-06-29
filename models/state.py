#!/usr/bin/python3
"""
    State Model
    HolbertonBnB
"""
from models.base_model import BaseModel


class State(BaseModel):
    """ User class for HBNB """

    def __init__(self, *args, **kwargs):
        """ constructor for User """
        '''from models import storage'''
        self.name = ""
        super().__init__(**kwargs)
