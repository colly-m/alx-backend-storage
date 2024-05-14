#!/usr/bin/env python3
"""Module to provide stats on nginx improving on the 12-log_stats.py"""
from pymongo import MongoClient


def stats_log():
    """Prints the log stats in nginx collection including top 10 IPs
    in the collection nginx of db logs"""
    client = MongoClient("mongodb://localhost:27017")
    logs_collection = client.logs.nginx
    total = logs_collection.count_documents({})
    get = logs_collection.count_documents({"method": "GET"})
    post = logs_collection.count_documents({"method": "POST"})
    put = logs_collection.count_documents({"method": "PUT"})
    patch = logs_collection.count_documents({"method": "PATCH"})
    delete = logs_collection.count_documents({"method": "DELETE"})
    path = logs_collection.count_documents(
        {"method": "GET", "path": "/status"})
    print(f"{total} logs")
    print("Methods:")
    print(f"\tmethod GET: {get}")
    print(f"\tmethod POST: {post}")
    print(f"\tmethod PUT: {put}")
    print(f"\tmethod PATCH: {patch}")
    print(f"\tmethod DELETE: {delete}")
    print(f"{path} status check")

    ten_ips = logs_collection.aggregate([
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ])

    print("\nTop 10 IPs:")
    for idx, ip_data in enumerate(ten_ips, 1):
        print(f"{idx}. {ip_data['_id']}: {ip_data['count']} request")


if __name__ == "__main__":
    stats_log()
