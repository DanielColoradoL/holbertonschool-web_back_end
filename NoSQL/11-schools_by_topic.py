#!/usr/bin/env python3
"""Task 11"""


def schools_by_topic(mongo_collection, topic):
    """returns the list of school having a specific topic"""
    output = []
    query = {"topics": topic}
    for doc in mongo_collection.find(query):
        print(doc)
        output.append(doc)
    return output
