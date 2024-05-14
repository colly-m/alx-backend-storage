#!/usr/bin/env python3
"""Module to provid stats on nginx"""
from pymongo import MongoClient


if __name__ == "__main__":
    """Prints the log stats in nginx collection"""
    client = MongoClient("mongodb://localhost:27017")
    logs_collection = client.logs.nginx

    print(f"{logs_collection.estimated_document_count()} logs")

    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    print('Methods:')

    for re in methods:
        print('\tmethods {}: {}'.format(re,
              logs_collection.count_documents({'method': re})))

    print('{} status check'.format(logs_collection.count_documents(
          {'method': 'GET', 'path': '/status'})))
