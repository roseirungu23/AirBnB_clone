#!/usr/bin/python3
"""Defines class user that inherets from BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """Represents class user that inherits from class BaseModel"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
