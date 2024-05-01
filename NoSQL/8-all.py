#!/usr/bin/env python3
"""Task 8"""


def list_all(mongo_collection):
    """lists all documents in a collection"""
    output = []
    if mongo_collection is None:
        return output
    for doc in mongo_collection.find():
        output.append(doc)
    return output
