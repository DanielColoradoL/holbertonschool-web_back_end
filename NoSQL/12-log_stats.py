#!/usr/bin/env python3
"""
Task 12
Provides some stats about Nginx logs
stored in MongoDB
All data was given, and it's avaiable on the intranet
"""

from pymongo import MongoClient


client = MongoClient('mongodb://127.0.0.1:27017')
collection = client.logs.nginx
total = collection.count_documents({})
print(f"{total} logs")

methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
print("Methods:")
for method in methods:
    count = collection.count_documents({"method": method})
    print(f"\tmethod {method}: {count}")

filt = {"method": "GET", "path": "/status"}
count = collection.count_documents(filt)
print(f"{count} status check")

client.close()
