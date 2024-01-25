import numpy as np

def policy(matrix, weight):
    """Compute Policy using Softmax Function"""
    logits = np.dot(matrix, weight)

    exp_logits = np.exp(logits)

    policy = exp_logits / np.sum(exp_logits, axis=1, keepdims=True)

    return policy

def policy_gradient(state, weight):
    """computes the Monte-Carlo policy gradient based on a state and a weight matrix."""
    policy_probs = policy(state, weight)

    action = np.random.choice(len(policy_probs[0]), p=policy_probs[0])
    softmax = np.diag(policy_probs.ravel()) - np.outer(policy_probs, policy_probs)
    grad = softmax[action]

    log = grad / policy_probs[None, action]
    s = log.reshape(1, -1)
    gradient = np.dot(state.T, s)

    return action, gradient
