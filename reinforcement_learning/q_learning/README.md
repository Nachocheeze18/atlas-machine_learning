## Reinforcement Learning Basics
# Markov Decision Process (MDP)
A Markov Decision Process is a mathematical framework used in reinforcement learning.

Components:

States (S): Set of possible environmental configurations.
Actions (A): Set of possible actions the agent can take.
Transition Probability (P): Probability of moving from one state to another given an action.
Reward Function (R): Immediate reward for taking a specific action in a particular state.
# Environment
The environment is the external context in which the agent operates, encompassing everything outside the agent that can influence or be influenced by its actions.

# Agent
An agent is the decision-making entity that interacts with the environment, aiming to maximize cumulative rewards.

# State
A state represents a particular configuration of the environment at a given moment.

# Policy Function
A policy function maps states to actions, defining the agent's behavior in the environment.

# Value Functions
State-Value Function (V(s)): Estimates expected cumulative future reward from a given state under a policy.
Action-Value Function (Q(s, a)): Estimates expected cumulative future reward from taking a specific action in a given state under a policy.
# Discount Factor
The discount factor (γ) influences the agent's preference for immediate rewards over delayed ones. It ranges between 0 and 1.

# Bellman Equation
The Bellman equation expresses the relationship between current and future values in reinforcement learning.

# Epsilon-Greedy
Epsilon-Greedy is a strategy balancing exploration and exploitation in reinforcement learning.

# Q-Learning
Q-Learning is a model-free reinforcement learning algorithm that learns an optimal action-value function without explicitly modeling the environment.