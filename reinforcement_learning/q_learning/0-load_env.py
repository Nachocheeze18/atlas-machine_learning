import gym

def load_frozen_lake(desc=None, map_name=None, is_slippery=False):
    if desc is not None or map_name is not None:
        env = gym.make('FrozenLake-v1', desc=desc, map_name=map_name, is_slippery=is_slippery)
    else:
        env = gym.make('FrozenLake-v1', is_slippery=is_slippery)
    
    return env