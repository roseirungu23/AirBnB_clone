#!/usr/bin/python3
"""Defines class City that inherits form BaseModel class"""
from models.base_model import BaseModel


class City(BaseModel):
    """Represents class City"""

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initializes class City"""
        super().__init__(*args, **kwargs)
