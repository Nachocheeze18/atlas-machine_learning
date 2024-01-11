import tensorflow as tf
import gym
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Flatten, Activation
from keras.optimizers import Adam
from rl.agents import DQNAgent
from rl.memory import SequentialMemory
from rl.policy import GreedyQPolicy
from rl.callbacks import Callback
import matplotlib.pyplot as plt
from IPython.display import display, clear_output

# Define a callback to record video during training
class RecordVideo(Callback):
    def __init__(self, env, filename, episode_trigger):
        self.env = env
        self.filename = filename
        self.episode_trigger = episode_trigger

    def on_episode_end(self, episode, logs):
        if self.episode_trigger(episode):
            self.env.unwrapped._monitor.close()
            self.env = gym.wrappers.Monitor(self.env, self.filename, force=True)

env_name = 'Breakout-v4'
weights_filename = 'policy.h5'
video_filename = '/content/drive/MyDrive/dqn/playdeepqbreakout.mp4'

# Modify the line below to include render_mode='rgb_array'
env = gym.make(env_name, render_mode='rgb_array')
env = RecordVideo(env, video_filename, episode_trigger=lambda episode: True)

np.random.seed(123)
env.env.seed(123)
nb_actions = env.env.action_space.n

model = Sequential()
model.add(Flatten(input_shape=(1,) + env.env.observation_space.shape))
model.add(Dense(16))
model.add(Activation('relu'))
model.add(Dense(16))
model.add(Activation('relu'))
model.add(Dense(16))
model.add(Activation('relu'))
model.add(Dense(nb_actions))
model.add(Activation('linear'))

memory = SequentialMemory(limit=1000000, window_length=1)
policy = GreedyQPolicy()

dqn = DQNAgent(model=model, nb_actions=nb_actions, policy=policy, memory=memory,
               nb_steps_warmup=50000, gamma=.99, target_model_update=10000,
               train_interval=4, delta_clip=1.)

optimizer = Adam(lr=0.001)
dqn.compile(optimizer=optimizer, metrics=['mae'])

dqn.load_weights(weights_filename)

# Parameters for rendering
num_episodes = 10
frames = []

for episode in range(num_episodes):
    state = env.env.reset()
    done = False
    episode_frames = []

    while not done:
        action = dqn.forward(state)
        state, _, done, _ = env.env.step(action)
        frame = env.env.render(mode='rgb_array')
        episode_frames.append(frame)

    frames.append(episode_frames)

env.close()

# Display the frames as a video
for episode_frames in frames:
    for frame in episode_frames:
        plt.imshow(frame)
        plt.axis('off')
        display(plt.gcf())
        clear_output(wait=True)
