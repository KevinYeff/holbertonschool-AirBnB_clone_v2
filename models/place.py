#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
#update relationship
from sqlalchemy.orm import relationship
from os import environ
import models

place_amenity = Table("place_amenity", Base.metadata,
                      Column("place_id", String(60), ForeignKey("places.id"), 
                             primary_key=True,
                             nullable=False),
                      Column("amenity_id", String(60),
                             ForeignKey("amenities.id"),
                             primary_key=True,
                             nullable=False))

class Place(BaseModel, Base):
    """Defines a Place Class, that has the new following attributes"""
    __tablename__ ="places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    #Update: add class attribute
    reviews = relationship("Review", backref="place", cascade="all")
    #Update: new class attribute
    amenities = relationship("Amenity", secondary="place_amenity", viewonly=False)
    
    if environ.get('HBNB_TYPE_STORAGE') != 'db':
        """ Attributes before update: A place to stay 
        update: Attributes restored"""
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []
        
        @property
        def reviews(self):
            
            from models.review import Review
            
            review_objs = []
            for review in models.storage.all(Review).values():
                if review.place_id == self.id:
                    review_objs.append(review)
            return review_objs
        
        #new getter and setter attributes
        @property
        def amenities(self):
            from models.amenity import Amenity
            amenity_objs = []
            for amenity in models.storage.all(Amenity).values():
                if amenity.place_id == self.amenity_ids:
                    amenity_objs.append(amenity)
            return amenity_objs
        
        # controlling what is going to be inside the amenity_ids list
        # only Amenity objects otherwise do nothing     
        @amenities.setter
        
        def amenities(self, value):
            """Setter for the amenities attribute."""
            from models.amenity import Amenity
            
            if isinstance(value, Amenity):
                self.amenity_ids.append(value.id)
        