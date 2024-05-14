#!/usr/bin/env python3
"""Module to return sort of average score"""


def top_students(mongo_collection):
    """
    Function to get all students score sorted
    mongo_collection: is the pymongo collection obj
    averageScore: key
    """
    top = [
        {
            "$project": {
                "name": "$name",
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {
            "$sort": {"averageScore": -1}
        }
    ]
    return list(mongo_collection.aggregate(top))
