#!/usr/bin/python3
"""
    File Storage Engine, choo choo!
    HolbertonBnB
"""
import json


class FileStorage():
    """ FileStorage class for command interpreter """

    def __init__(self):
        """ constructor for FS """
        self.__file_path = 'file.json'
        self.__objects = dict()

    def all(self):
        """ returns dict of __objects """
        return self.__objects

    def new(self, obj):
        """ new obj """
        self.__objects[str(type(self).__name__) + "." + str(obj['id'])] = obj

    def save(self):
        """ saves/seralizes up in this motherfucker """
        fn = "file.json"
        e = self.__objects
        for key in list(e.keys()):
            e[key]['created_at'] = str(e[key]['created_at'])
            e[key]['updated_at'] = str(e[key]['updated_at'])
        d = json.dumps(e)
        with open(fn, 'w', encoding='utf-8') as f:
            f.write(d)

    def reload(self):
        """ deserializer, up in this bitch """
        fn = "file.json"
        try:
            with open(fn, 'r', encoding='utf-8') as f:
                s = f.read()
                l = json.loads(s)
                self.__objects = l
        except FileNotFoundError:
            pass
