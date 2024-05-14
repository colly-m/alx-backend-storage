#!/usr/bin/env python3
"""Module to insert a new doc in a collection"""


def insert_school(mongo_collection, **kwargs):
    """Function to insert a document based on kwargs"""
    new_Doc = mongo_collection.insert_one(kwargs)

    return new_Doc.inserted_id
