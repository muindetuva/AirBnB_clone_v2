#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
import os
from sqlalchemy import Column, String


class User(BaseModel, Base):
    """
    This class defines a user by various attributes
    Attributes:
        __tablename__(str): The name of the table
        email(str): User's email cant be null
        password(str): The user password, cant be null
        first_name(str): User's first name
        last_name(str): User's last name
    """
    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=False)
        last_name = Column(String(128), nullable=False)
    else:
        email = ''
        password = ''
        first_name = ''
        last_name = ''

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)
