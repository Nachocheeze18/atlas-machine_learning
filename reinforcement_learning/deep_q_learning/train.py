import gym
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Activation, Flatten
from gym.wrappers import RecordVideo
from keras.optimizers import Adam
from rl.agents.dqn import DQNAgent
from rl.policy import EpsGreedyQPolicy, LinearAnnealedPolicy
from rl.memory import SequentialMemory
from keras.callbacks import Callback
import json

class CustomModelCheckpoint(Callback):
    def __init__(self, filepath, monitor='val_loss', verbose=0, save_best_only=False,
                 save_weights_only=False, mode='auto', period=1):
        super(CustomModelCheckpoint, self).__init__()
        self.filepath = filepath
        self.monitor = monitor
        self.verbose = verbose
        self.save_best_only = save_best_only
        self.save_weights_only = save_weights_only
        self.period = period
        self.epochs_since_last_save = 0
        self.best = np.Inf if 'loss' in monitor else -np.Inf
        self.train_logs = {'episode_reward': []}

    def on_train_begin(self, logs=None):
        self.train_logs = {'episode_reward': []}

    def on_step_end(self, step, logs=None):
        episode_reward = logs['episode_reward'] if 'episode_reward' in logs else None
        if episode_reward is not None:
            self.train_logs['episode_reward'].append(episode_reward)

    def on_epoch_end(self, epoch, logs=None):
        logs = logs or {}
        self.epochs_since_last_save += 1
        if self.epochs_since_last_save >= self.period:
            self.epochs_since_last_save = 0
            filepath = self.filepath.format(epoch=epoch + 1, **logs)
            if self.save_best_only:
                current = logs.get(self.monitor)
                if current is None:
                    pass
                else:
                    if self.monitor_op(current, self.best):
                        self.best = current
                        if self.verbose > 0:
                            print(f'\nEpoch {epoch + 1}: {self.monitor} improved from '
                                  f'{self.best:.5f} to {current:.5f}, saving model to {filepath}')
                        if self.save_weights_only:
                            self.model.save_weights(filepath, overwrite=True)
                        else:
                            self.model.save(filepath, overwrite=True)
                    else:
                        if self.verbose > 0:
                            print(f'\nEpoch {epoch + 1}: {self.monitor} did not improve')

            else:
                if self.verbose > 0:
                    print(f'\nEpoch {epoch + 1}: saving model to {filepath}')
                if self.save_weights_only:
                    self.model.save_weights(filepath, overwrite=True)
                else:
                    self.model.save(filepath, overwrite=True)

# Environment setup
env = gym.make('Breakout-v4')
env = RecordVideo(env, '/content/drive/MyDrive/dqn/deepqbreakout.mp4', episode_trigger=lambda episode: True)
np.random.seed(123)
env.seed(123)
nb_actions = env.action_space.n

# Build a simple model
model = Sequential()
model.add(Flatten(input_shape=(1,) + env.observation_space.shape))
model.add(Dense(16))
model.add(Activation('relu'))
model.add(Dense(nb_actions))
model.add(Activation('linear'))

# Configure and compile our agent
memory = SequentialMemory(limit=1000000, window_length=1)
policy = LinearAnnealedPolicy(EpsGreedyQPolicy(), attr='eps',
                              value_max=1., value_min=.1,
                              value_test=.05, nb_steps=5000)

agent = DQNAgent(model=model, nb_actions=nb_actions, memory=memory, nb_steps_warmup=10000,
               target_model_update=1e-2, policy=policy)
agent.compile(Adam(lr=1e-3), metrics=['mae'])

# Define the custom callback for logging
checkpoint = CustomModelCheckpoint('policy.h5', monitor='mae', verbose=1,
                                   save_best_only=True, mode='min', period=1)

# Train the agent
agent.fit(env, nb_steps=5000, visualize=False, verbose=2, callbacks=[checkpoint])

# Save the training logs to a JSON file
with open('training_log.json', 'w') as f:
    json.dump(checkpoint.train_logs, f)
