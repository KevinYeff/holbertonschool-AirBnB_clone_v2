#!/usr/bin/python3
"""New engine DBStorage"""
# to get enviromental variables
from os import environ
# to create the engine
from sqlalchemy import create_engine
# create_engine syntaxis: [dialect]+[driver]://[username]:[password]@[host]:[port]/[database]


class DBStorage():
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
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:{}/{}'.format(environ.get("HBNB_MYSQL_USER"),
                                                                              environ.get("HBNB_MYSQL_PWD"),
                                                                              environ.get("HBNB_MYSQL_HOST"),
                                                                              environ.get("HBNB_MYSQL_DB")))
        