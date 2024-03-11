#!/usr/bin/python3
"""The User module, about data related to user"""
from models.base_model import BaseModel


class User(BaseModel):
    """the user class
    used to create and update user data
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
