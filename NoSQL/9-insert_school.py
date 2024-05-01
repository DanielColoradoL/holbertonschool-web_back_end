#!/usr/bin/env python3
"""Task 9"""


def insert_school(mongo_collection, **kwargs):
    """inserts a new document in a collection based on kwargs"""
    obj = mongo_collection.insert_one(kwargs)
    return obj.inserted_id
