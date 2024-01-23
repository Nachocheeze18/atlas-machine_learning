#!/usr/bin/env python3
"""Imports"""
import numpy as np


def monte_carlo(env, V, policy, episodes=5000, max_steps=100, alpha=0.1, gamma=0.99):
    """performs the Monte Carlo algorithm"""
    for _ in range(episodes):
        state, _ = env.reset()
        states, rewards = [], []

        for _ in range(max_steps):
            action = policy(state)
            state, reward, done, _, _ = env.step(action)
            states.append(state)
            rewards.append(reward)

            if done: break

        G = 0
        for t in range(len(states) - 1, -1, -1):
            G = gamma * G + rewards[t]
            V[states[t]] += alpha * (G - V[states[t]])

    return V
