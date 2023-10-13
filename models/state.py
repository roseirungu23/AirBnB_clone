#!/usr/bin/python3
"""Defines class State that inherits from class BaseModel"""
from models.base_model import BaseModel


class State(BaseModel):
    """Represents class State"""

    name = ""

    def __init__(self, *args, **kwargs):
        """Initializes class State"""
        super().__init__(*args, **kwargs)
