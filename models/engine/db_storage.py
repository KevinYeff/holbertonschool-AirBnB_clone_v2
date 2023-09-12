#!/usr/bin/python3
"""New engine DBStorage"""

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
        pass