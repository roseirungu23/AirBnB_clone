#!/usr/bin/python3
"""Defines class Review inhereted from class BaseModel"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Class Review inherits from BaseModel and represents a review"""

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """initializes class Review"""
        super().__init__(*args, **kwargs)
