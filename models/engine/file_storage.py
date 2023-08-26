#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
import models
from os import path


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns a dictionary of models currently in storage"""
        return FileStorage.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        key = obj.to_dict()['__class__'] + '.' + obj.id
        self.all().update({key: obj})

    def save(self):
        """Saves storage dictionary to file"""

        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f, indent=2, sort_keys=True)

    def reload(self):
        """Loads storage dictionary from file"""
        file_path = self.__file_path
        if path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as f:
                self.__objects = json.load(f)
                for key, value in self.__objects.items():
                    extract_cls_name = value["__class__"]
                    check_cls_in_var = models.classes[extract_cls_name]
                    simple_instance = check_cls_in_var(**value)
                    self.__objects[key] = simple_instance
