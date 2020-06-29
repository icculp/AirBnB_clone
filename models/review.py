#!/usr/bin/python3
"""
    Review Model
    HolbertonBnB
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """ User class for HBNB """

    def __init__(self, *args, **kwargs):
        """ constructor for User """
        '''from models import storage'''
        self.place_id = ""
        self.user_id = ""
        self.text = ""
        super().__init__(**kwargs)
