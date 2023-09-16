#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class User(BaseModel, Base):
    """This class defines a User with the new following class attributes"""
    
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name= Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)    
    places = relationship("Place", backref="user", cascade="all")
    #update: add class attribute
    reviews = relationship("Review", backref="user", cascade="all")
    """Attributes before update. This class defines a user by various attributes
    email = ''
    password = ''
    first_name = ''
    last_name = ''
    """