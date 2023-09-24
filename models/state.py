#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column, ForeignKey
from models.city import City
from sqlalchemy.orm import relationship
from models import storage_type


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="states",
                          cascade="all, delete-orphan")

    if storage_type != "db":
        @property
        def cities(self):
            """Getter attribute cities that returns the list of City instances

            Returns:
                list of objects
            """
            from models import storage
            my_list = []
            rel_cities = storage.all(City).values()
            for city in rel_cities:
                if self.id == city.state_id:
                    my_list.append(city)
            return my_list
