#!/usr/bin/python3
"""
Initializes the models package based on the storage type defined in environment variable HBNB_TYPE_STORAGE.
"""

from os import getenv
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage

storage_type = getenv("HBNB_TYPE_STORAGE")

if storage_type == "db":
    storage = DBStorage()
else:
    storage = FileStorage()

storage.reload()
