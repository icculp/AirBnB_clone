#!/usr/bin/python3
"""
    Amenity Model
    HolbertonBnB
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ User class for HBNB """

    def __init__(self, *args, **kwargs):
        """ constructor for User """
        '''from models import storage'''
        self.name = ""
        super().__init__(**kwargs)
