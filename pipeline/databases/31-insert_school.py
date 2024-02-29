#!/usr/bin/env python3
"""insert new"""
def insert_school(mongo_collection, **kwargs):
    """Insert the document into the collection"""
    new_document = mongo_collection.insert_one(kwargs)
    return new_document.inserted_id
