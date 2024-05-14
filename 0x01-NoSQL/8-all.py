#!/usr/bin/env python3
"""Module to list all docs in a collection"""


def list_all(mongo_collection):
    """Function to make a list of all documents in list"""
    cursor = mongo_collection.find()

    return [docs for docs in cursor]
