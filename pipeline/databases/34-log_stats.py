#!/usr/bin/env python3
"""Imports"""
from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client['logs']
    nginx_collection = db['nginx']

    total_logs = nginx_collection.count_documents({})
    print(f"{total_logs} logs")
    print("Methods:")

    http_methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_stats_dict = {}

    for method in http_methods:
        method_count = nginx_collection.count_documents({"method": method})
        method_stats_dict[method] = method_count

    for method, count in method_stats_dict.items():
        print(f"\tmethod {method}: {count}")

    status_check_count = nginx_collection.count_documents({'method': 'GET', 'path': "/status"})
    print(f"{status_check_count} status check")