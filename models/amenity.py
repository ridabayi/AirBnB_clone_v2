#!/usr/bin/python3
"""
Contains the Amenity class
"""

import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String


class Amenity(BaseModel, Base):
    """Representation of an Amenity."""

    if models.storage_t == 'db':
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """Initializes an Amenity instance."""
        super().__init__(*args, **kwargs)
