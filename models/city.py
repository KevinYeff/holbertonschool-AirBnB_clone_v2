#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import String


class City(BaseModel, Base):
    """ The city class, contains state ID and name 
    update: now will have new attributes to link to 
    a MySQL table"""
    
    # new class attribute:
    __tablename__ = "cities"
    # attributes order changed
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("state.id"), nullable=False,)
    