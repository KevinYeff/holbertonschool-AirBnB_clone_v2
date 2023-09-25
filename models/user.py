#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import environ

if environ.get('HBNB_TYPE_STORAGE') == 'db':
    class User(BaseModel, Base):
        """This class defines a User with the new following class attributes"""
        
        __tablename__ = "users"
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name= Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)    
        places = relationship("Place", backref="user", cascade="all")
        #update: add class attribute
        reviews = relationship("Review", backref="user", cascade="all")
else:
    class User(BaseModel):
        
        """Attributes before update. This class defines a user by various attributes"""
        email = ''
        password = ''
        first_name = ''
        last_name = ''
        