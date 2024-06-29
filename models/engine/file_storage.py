#!/usr/bin/python3
"""
Contains the FileStorage class
"""

import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class FileStorage:
    """Serializes instances to a JSON file & deserializes back to instances"""

    __file_path = "file.json"  # Path to the JSON file
    __objects = {}  # Dictionary to store all objects by <class name>.id

    def all(self, cls=None):
        """Returns the dictionary __objects"""
        if cls:
            if isinstance(cls, str):
                cls = classes.get(cls, None)
            if cls:
                return {key: obj for key, obj in self.__objects.items()
                        if isinstance(obj, cls)}
            return {}
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        json_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(json_dict, file)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                json_dict = json.load(file)
                self.__objects = {}
                for key, value in json_dict.items():
                    cls_name = value['__class__']
                    if cls_name in classes:
                        self.__objects[key] = classes[cls_name](**value)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Deletes obj from __objects if it exists"""
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects.pop(key, None)

    def close(self):
        """Calls reload() method for deserializing the JSON file to objects"""
        self.reload()
