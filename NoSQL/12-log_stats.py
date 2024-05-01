#!/usr/bin/env python3
"""
Task 12
Provides some stats about Nginx logs
stored in MongoDB
All data was given, and it's avaiable on the intranet
"""
from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx
    total = collection.count_documents({})
    print("{} logs".format(total))

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = collection.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, count))

    filt = {"method": "GET", "path": "/status"}
    count = collection.count_documents(filt)
    print("{} status check".format(count))

    client.close()
