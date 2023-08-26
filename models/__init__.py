#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage
from .base_model import BaseModel
from .user import User
from .state import State
from .city import City
from .amenity import Amenity
from .place import Place
from .review import Review

classes = {
    'BaseModel': BaseModel, 'User': User, 'Place': Place,
    'State': State, 'City': City, 'Amenity': Amenity,
    'Review': Review
}

dot_cmds = ['all', 'count', 'show', 'destroy', 'update']

types = {
    'number_rooms': int, 'number_bathrooms': int,
    'max_guest': int, 'price_by_night': int,
    'latitude': float, 'longitude': float
}

storage = FileStorage()
storage.reload()
