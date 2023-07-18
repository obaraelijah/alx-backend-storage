#!/usr/bin/env python3
'''Python function that returns the list of school having a specific topi.'''


def schools_by_topic(mongo_collection, topic):
    """Returns the list of school having a specific topic"""
    return mongo_collection.find({"topics": topic})
