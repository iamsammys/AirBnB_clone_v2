#!/usr/bin/python3
"""module to implement the database storage engine
"""
from models.base_model import Base, BaseModel
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import os

user = os.getenv("HBNB_MYSQL_USER")
host = os.getenv("HBNB_MYSQL_HOST")
pwd = os.getenv("HBNB_MYSQL_PWD")
db = os.getenv("HBNB_MYSQL_DB")
env = os.getenv("HBNB_ENV")


class DBStorage:
    """Class for database engine
    """
    __engine = None
    __session = None

    def __init__(self):
        """instantiates the DBStorage class objects
        """
        DBStorage.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format(
            user, pwd, host, db), pool_pre_ping=True)
        if env == "test":
            Base.metadata.drop_all()

    def all(self, cls=None):
        """Returns all the objects of a class from the database
        """
        dictionary = {}
        if cls is None:
            for clss in classes:
                result = DBStorage.__session.query(clss).all()
                for row in result:
                    key = "{}.{}".format(row.__class__.__name__, rows.id)
                    dictionary[key] = row
        elif cls in classes:
            for row in DBStorage.__session.query(cls).all():
                key = "{}.{}".format(row.__class__.__name__, rows.id)
                dictionary[key] = row
        return dictionary

    def new(self, obj=None):
        """Adds instance to the current database session
        """
        DBStorage.__session.add(obj)

    def save(self):
        """Commits all changes of the current database session
        """
        DBStorage.__session.commit()
    
    def delete(self, obj=None):
        """Delete from the current database session obj if not None
        """
        DBStorage.__session.delete(obj)

    def reload(self):
        """Creates the current database session
        """
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine,
                               expire_on_commit=False)
        Scoped_session = scoped_session(Session)
        DBStorage.__session = Scoped_session()
