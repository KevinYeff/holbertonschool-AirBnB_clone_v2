#!/usr/bin/python3
"""New engine DBStorage"""
# to get enviromental variables
from os import environ
# to create the engine
from sqlalchemy import create_engine
# create_engine syntaxis: [dialect]+[driver]://[username]:[password]@[host]:[port]/[database]
#to delete all tables if we are in a test enviroment
from models.base_model import Base 
# retrieving all the classes
from models import classes

class DBStorage:
    """New class that represents an storage engine and has the
    following attributes"""
    __engine = None
    __session = None
    
    #public instance method
    def __init__(self):
        """This method creates the engine, the engine must be linked
        to the MySQL database and user created in previus tasks
        hbnb_dev and hbnb_dev_db"""
        # creating engine using the enviromental variables (retrieving values vía enviromental variables)
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(environ.get("HBNB_MYSQL_USER"),
                                                                              environ.get("HBNB_MYSQL_PWD"),
                                                                              environ.get("HBNB_MYSQL_HOST"),
                                                                              environ.get("HBNB_MYSQL_DB")), 
                                      pool_pre_ping=True)
        #avoiding te accidental elimination of data in a production or dev enviroment
        if environ.get('HBNB_ENV') == 'test':
            Base.metadata.drop_all()
        
        def all(self, cls=None):
            """Retrieves objects from the database based on the class name provided.
            Returns a dictionary just like Filestorage"""
            #empty dict to store the objects
            objects_dict = {}
            
            # make sure that we are in a database session
            if self.__session is None:
                print("** no session established **")
                return {}
            
            #quering all types of objects when no class is passed
            if cls is None:
                for class_name, clase in classes.items():
                    #query all types
                    cls_objs = self.__session.query(clase).all()
                    for object in cls_objs:
                        # add the objecto to the dictionary
                        objects_dict[f"{cls.__name__}.{object.id}"] = object
            else:
                # if there is a specific class query it
                cls_objs = self.__session.query(cls).all()
                # add the obj of the specified class to the dictionary
                for object in cls_objs:
                    objects_dict[f"{cls.__name__}.{object.id}"] = object
            
            #return the dictionary
            return objects_dict
        