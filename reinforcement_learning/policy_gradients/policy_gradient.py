import numpy as np

def policy(matrix, weight):
    """Compute Policy using Softmax Function"""
    logits = np.dot(matrix, weight)

    exp_logits = np.exp(logits)

    computed_policy = exp_logits / np.sum(exp_logits, axis=1, keepdims=True)

    return computed_policy

def policy_gradient(state, weight):
    """computes the Monte-Carlo policy gradient based on a state and a weight matrix"""
    action_probs = policy(state, weight)

    action = np.random.choice(len(action_probs[0]), p=action_probs[0])

    reshaped_probs = action_probs.reshape(-1, 1)

    soft_matrix = np.diagflat(reshaped_probs) - np.outer(reshaped_probs, reshaped_probs.T)[action, :]

    log_ratio = soft_matrix / action_probs[0, action]

    gradient = state.T.dot(log_ratio[None, :])

    return action, gradient