#!/usr/bin/python3
"""
    File Storage Engine, choo choo!
    HolbertonBnB
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.city import City
from models.state import State
from models.review import Review


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
        self.__objects[str(type(obj).__name__) + "." +
                       str(obj.__dict__['id'])] = obj

    def save(self):
        """ saves/seralizes up in this motherfucker """
        e = dict(self.__objects)
        '''self.reload()'''
        '''print("299999999")
        print(e)'''
        for key in list(e.keys()):
            e[key] = dict(e[key].to_dict())
            """e[key] = dict(e[key].__dict__)
            e[key]['created_at'] = e[key]['created_at'].now().isoformat()
            e[key]['updated_at'] = e[key]['updated_at'].now().isoformat()"""
        d = json.dumps(e)
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            f.write(d)
        '''self.reload()'''

    def reload(self):
        """ deserializer, up in this bitch """
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                s = f.read()
                l = json.loads(s)
                list_of_classes = ['BaseModel', 'User', 'State',
                                   'City', 'Amenity', 'Place', 'Review']
                for key in list(l.keys()):
                    for i in list_of_classes:
                        if i in key:
                            c = i + '(**l[key])'
                            self.__objects[key] = eval(c)
                        """if "BaseModel" in key:
                            self.__objects[key] = BaseModel(**l[key])
                        elif "User" in key:
                            self.__objects[key] = User(**l[key])"""
        except FileNotFoundError:
            pass
