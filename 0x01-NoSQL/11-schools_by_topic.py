#!/usr/bin/env python3
"""Module to return list of school having special topic"""


def schools_by_topic(mongo_collection, topic):
    """Function to return list of topic"""
    return mongo_collection.find({"topics": topic})
