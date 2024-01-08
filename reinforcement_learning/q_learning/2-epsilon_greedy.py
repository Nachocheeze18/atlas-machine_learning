#!/usr/bin/env python3
"""Imports"""
import numpy as np


def epsilon_greedy(Q, state, epsilon):
    """Epsilon-greedy strategy to determine the next action."""
    exp = np.random.uniform() < epsilon

    if exp:
        action = np.random.randint(Q.shape[1])
    else:
        action = np.argmax(Q[state, :])

    return action
