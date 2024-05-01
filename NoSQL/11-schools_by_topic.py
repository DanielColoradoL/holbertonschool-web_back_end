#!/usr/bin/env python3
"""Task 11"""


def schools_by_topic(mongo_collection, topic):
    """returns the list of school having a specific topic"""
    output = []
    query = {"topics": {"$in": [topic]}}
    for doc in mongo_collection.find(query):
        output.append(doc)
    return output
