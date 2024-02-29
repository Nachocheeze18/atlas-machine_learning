#!/usr/bin/env python3
"""specific topic"""
def schools_by_topic(mongo_collection, topic):
    """returns the list of school having a specific topic"""
    schools = mongo_collection.find({"topics": {"$in": [topic]}})
    school_names = [school["name"] for school in schools]
    
    return school_names
