#!/usr/bin/env python3
"""Imports"""
import pandas as pd


data = {
    'First': [0.0, 0.5, 1.0, 1.5],
    'Second': ['one', 'two', 'three', 'four']
}
index_labels = ['A', 'B', 'C', 'D']
df = pd.DataFrame(data, columns=['First', 'Second'],
                  index=index_labels)