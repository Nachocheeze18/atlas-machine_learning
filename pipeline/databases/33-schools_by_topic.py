#!/usr/bin/env python3
"""specific topic"""
def schools_by_topic(mongo_collection, topic):
    """returns the list of school having a specific topic"""
    specific_topic = mongo_collection.find({"topics": topic})
    return specific_topic