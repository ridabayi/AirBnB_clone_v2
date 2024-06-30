#!/usr/bin/python3
""" Holds class City """

import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ Representation of a city """

    __tablename__ = 'cities'  # Table name for database storage

    if models.storage_t == "db":
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        name = Column(String(128), nullable=False)
        places = relationship("Place", backref="cities")
    else:
        state_id = ""  # Placeholder for non-database storage
        name = ""      # Placeholder for non-database storage

    def __init__(self, *args, **kwargs):
        """ Initializes City """
        super().__init__(*args, **kwargs)
