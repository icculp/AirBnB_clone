#!/usr/bin/python3
"""
    File Storage Engine, choo choo!
    HolbertonBnB
"""
import json
from models.base_model import BaseModel


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
        self.__objects[str(type(obj).__name__) + "." + str(obj.__dict__['id'])] = obj

    def save(self):
        """ saves/seralizes up in this motherfucker """
        fn = "file.json"
        e = self.__objects
        print("-------------")
        print(e)
        for key in list(e.keys()):
            print("-----------------------")
            print(e[key])
            e[key] = e[key].__dict__
            e[key]['created_at'] = e[key]['created_at'].now().isoformat()
            e[key]['updated_at'] = e[key]['updated_at'].now().isoformat()
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
                '''self.__objects = l'''
                for key in list(l.keys()):
                    self.__objects[key] = BaseModel(**l[key])
        except FileNotFoundError:
            pass
