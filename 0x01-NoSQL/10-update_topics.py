#!/usr/bin/env python3
"""Module to change all school topics based on there name"""


def update_topics(mongo_collection, name, topics):
    """
    Function to change all topics
    mongo_collection: will be pymongo collection obj
    name: school name to update(string)
    topics: list of topics approached in the school
    """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
