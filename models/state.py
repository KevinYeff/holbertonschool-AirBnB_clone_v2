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
    
    # getter attribute when filestorage is used instead of dbstorage
    @property
    def cities(self):
        """Getter attribute that returns a list of city instances """
        # storage variableimported
        from models import storage
        #implement an empty list
        city_lsit = []
        # iterate through the City instances
        for city in storage.all(City).values():
            #in the previous task we update the state_id (class attribute)
            if city.state_id == self.id:
                # Add cities that are related to state (current) to the list
                city_lsit.append(city)
        # return that list        
        return city_lsit    
