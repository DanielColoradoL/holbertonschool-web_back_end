#!/usr/bin/env python3
"""Task 10"""


def update_topics(mongo_collection, name, topics):
    """changes all topics of a school document based on the name"""
    filt = {"name": name}
    new_values = {"$set": {'topics': topics}}
    mongo_collection.update_one(filt, new_values)
