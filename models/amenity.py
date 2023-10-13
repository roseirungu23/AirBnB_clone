#!/usr/bin/python3
"""Defines class Amenity that inherits from class BaseModel"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represents class Amenity"""

    name = ""

    def __init__(self, *args, **kwargs):
        """Initializes class Amenity"""
        super().__init__(*args, **kwargs)

