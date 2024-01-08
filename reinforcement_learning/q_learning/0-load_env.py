#!/usr/bin/env python3
"""Imports"""
import gym
from gym.envs.toy_text.frozen_lake import generate_random_map


def load_frozen_lake(desc=None, map_name=None, is_slippery=False):
    """Loads the pre-made FrozenLakeEnv environment from OpenAIs gym."""
    if desc is None and map_name is None:
        desc = generate_random_map(size=8)
    
    env = gym.make('FrozenLake-v1', desc=desc, map_name=map_name, is_slippery=is_slippery)

    return env