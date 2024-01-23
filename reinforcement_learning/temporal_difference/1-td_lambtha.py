#!/usr/bin/env/python3
"""Imports"""
import numpy as np


def td_lambtha(env, V, policy, lambtha, episodes=5000, max_steps=100, alpha=0.1, gamma=0.99):
    """TD(λ) algorithm for updating value estimates."""
    for _ in range(episodes):
        state, _ = env.reset()
        eligibility_trace = np.zeros_like(V)

        for _ in range(max_steps):
            action = policy(state)
            state, reward, done, _, _ = env.step(action)

            delta = reward + gamma * V[state] - V[state]
            eligibility_trace[state] += 1

            for s in range(len(V)):
                V[s] += alpha * delta * eligibility_trace[s]
                eligibility_trace[s] *= gamma * lambtha

            if done:
                break

    return V
