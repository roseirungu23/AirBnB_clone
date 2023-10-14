#!/usr/bin/python3
"""Defines class FileStorage""" 

import json

class FileStorage:
    """Initializes class FileStorage"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Public instance method that returns the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Public instance method that sets in __objects"""
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            FileStorage.__objects[key] = obj

    def save(self):
        """Public instance method that serializes __objects to the JSON file (path: __file_path)"""
        new_dict = {}
        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict().copy()

        with open(FileStorage.__file_path, mode='w') as my_file:
            json.dump(new_dict, my_file)

    def reload(self):
        """Public instance method that deserializes a JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, mode='r') as my_file:
                new_dict = json.load(my_file)

            for key, value in new_dict.items():
                class_name = value.get('__class__')
                obj = eval(class_name + '(**value)')
                FileStorage.__objects[key] = obj

        except FileNotFoundError:
            pass
