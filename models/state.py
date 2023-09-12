#!/usr/bin/python3
""" State Module for HBNB project """
#now inherits also from Base
from models.base_model import BaseModel, Base
#importing column ans string for table attributes
from sqlalchemy import Column, String
#for relationship
from models.city import City
from sqlalchemy.orm import relationship



class State(BaseModel):
    """ State class 
    update: now will have new attributes to link to 
    a MySQL table"""
    
    #new class attribute
    __tablename__ = "states"
    #class attribute changed
    name = Column(String(128), nullable=False)
    #for dbstorage relationship
    cities = relationship("City", backref="state", cascade="delete")
    
    # getter attribute whe filestorage is used instead of dbstorage
    @property
    def cities(self):
        """No documentation yet"""
        return []    
