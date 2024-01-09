#!/usr/bin/env python3
"""Imports"""
import numpy as np
epsilon_greedy = __import__('2-epsilon_greedy').epsilon_greedy


def train(env, Q, episodes=5000, max_steps=100, alpha=0.1, gamma=0.99, epsilon=1, min_epsilon=0.1, epsilon_decay=0.05):
    """performs Q-learning"""
    total_rewards = []

    episode = 0
    while episode < episodes:
        state, _ = env.reset()
        episode_reward = 0
        step = 0

        while step < max_steps:
            if np.random.rand() < epsilon:
                action = env.action_space.sample()
            else:
                action = np.argmax(Q[state, :])

            next_state, reward, done, _, _ = env.step(action)

            Q[state, action] = (1 - alpha) * Q[state, action] + alpha * (reward + gamma * np.max(Q[next_state, :]))
            episode_reward += reward
            state = next_state

            if done:
                break

            step += 1

        epsilon = max(min_epsilon, epsilon - epsilon_decay)
        total_rewards.append(episode_reward)
        episode += 1

    return Q, total_rewards
