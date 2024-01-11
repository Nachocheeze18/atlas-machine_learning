import tensorflow as tf
import gym
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Flatten, Activation
from keras.optimizers import Adam
from rl.agents import DQNAgent
from rl.memory import SequentialMemory
from rl.policy import EpsGreedyQPolicy
from keras.callbacks import ModelCheckpoint

env_name = 'Breakout-v4'
weights_filename = 'policy.h5'

env = gym.make(env_name)
np.random.seed(123)
env.seed(123)
nb_actions = env.action_space.n

model = Sequential()
model.add(Flatten(input_shape=(1,) + env.observation_space.shape))
model.add(Dense(16))
model.add(Activation('relu'))
model.add(Dense(16))
model.add(Activation('relu'))
model.add(Dense(16))
model.add(Activation('relu'))
model.add(Dense(nb_actions))
model.add(Activation('linear'))

memory = SequentialMemory(limit=1000000, window_length=1)
policy = EpsGreedyQPolicy()

dqn = DQNAgent(model=model, nb_actions=nb_actions, policy=policy, memory=memory,
               nb_steps_warmup=50000, gamma=.99, target_model_update=10000,
               train_interval=4, delta_clip=1.)
dqn.compile(Adam(lr=1e-3), metrics=['mae'])

checkpoint = ModelCheckpoint(weights_filename, monitor='mae', verbose=1,
                             save_best_only=True, mode='min', period=1)

callbacks = [checkpoint]

dqn.fit(env, nb_steps=5000, visualize=False, callbacks=callbacks, verbose=2)

dqn.save_weights(weights_filename, overwrite=True)
