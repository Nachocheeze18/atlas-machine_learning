#!/usr/bin/env python3
"""Imports"""
import pandas as pd
import numpy as np


def from_numpy(array):
    """creates a pd.DataFrame from a np.ndarray"""
    column_names = [chr(i) for i in range(ord('A'), ord('Z')+1)]
    
    df = pd.DataFrame(array, columns=column_names[:array.shape[1]])
    
    return df
