#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City

class State(BaseModel):
    """
    State class
    Attributes:
        __tablename__(str): Maps to the table name
        name(str): The name of the State
        cities: Relationship between city and state
    """
    if os.getenv('HBNB_TYPE_STORAGE') == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="all, delete, \
                               delete-orphan")
    else:
        name = ""

        @property
        def cities(self):
            '''A getter method for cities from file storage'''
            cities = storage.all(City).values()
            cities_list = [city for city in cities if self.id == city.state_id]
            return cities_list
