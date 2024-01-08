#!/usr/bin/env python3
"""Imports"""
import numpy as np


def q_init(env):
    """Initializes the Q-table for a given environment."""
    Q_table = np.zeros((env.observation_space.n, env.action_space.n))
    return Q_table
