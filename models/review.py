#!/usr/bin/python3
"""the review module
collect the customers reviews
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """data related to customers reviews"""

    place_id = ""
    user_id = ""
    text = ""
