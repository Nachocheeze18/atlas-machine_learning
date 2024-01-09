#!/usr/bin/env python3
"""Imports"""
import numpy as np


def play(env, Q, max_steps=100):
    """the trained agent play an episode"""
    state, _ = env.reset()
    total_rewards = 0
    step = 0

    while step < max_steps:
        action = np.argmax(Q[state, :])

        next_state, total_rewards, done, _, _ = env.step(action)

        env.render()

        state = next_state
        step += 1

        if done:
            break

    return total_rewards
