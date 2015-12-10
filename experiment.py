import argparse
import os
import cPickle
import numpy as np
import time

import agent
import q_network
import simulator     # LF2

# TODO

# argparse
###### Q NETWORK ######
input_width, input_height = [100,100]
num_actions = 10
phi_length = 4 # phi length?  input 4 frames at once
discount = 0.95
learning_rate = 0.00025
rms_decay = 0.99 # rms decay
rms_epsilon = 0.1
momentum = 0
clip_delta = 1.0
freeze_interval = 10000 #???  no freeze?
batch_size = 32
network_type = 'nature_dnn'
update_rule = 'deepmind_rmsprop' # need update
batch_accumulator = 'sum'
rng = np.random.RandomState()
###### AGENT ######
epsilon_start = 1.0
epsilon_min = 0.1
epsilon_decay = 1000000
replay_memory_size = 1000000
experiment_prefix = 'LF2'
replay_start_size = 50000
update_frequency = 4  #??
#######################

class experiment():
  def __init__(self,agent,env):
    self.agent = agent
    self.env = env

  #def run():
  #  for epoch in xrange(num_epoch):
  #    self.run_epoch()             # train
  #    self.run_epoch()    # test

  #def run_epoch():
  #  while steps_left > 0:
  #    num_steps = self.run_episode(steps_left, testing)

  def run_episode(self,max_steps):
    self.env.reset_game()
    print 'aja'
    action = self.agent.start_episode(self.env.get_observation())
    #action = self.agent.start_episode(np.random.rand(200,200))
    num_steps = 0

    while True:
      [reward, screen] = self.env.step(action)
      #reward = np.random.rand(1)
      #screen = np.random.rand(200,200)
      #terminal = self.env.game_over()
      terminal = False
      num_steps += 1

      if num_steps >= max_steps:  # or terminal
        self.agent.end_episode(reward, terminal)
        break

      action = self.agent.step(reward, screen)
      print action
    return num_steps

def launch():
  t = time.time()
  network = q_network.DeepQLearner(input_width, input_height, num_actions,
                                         phi_length,
                                         discount,
                                         learning_rate,
                                         rms_decay,
                                         rms_epsilon,
                                         momentum,
                                         clip_delta,
                                         freeze_interval,
                                         batch_size,
                                         network_type,
                                         update_rule,
                                         batch_accumulator,
                                         rng)
  print 'compile network done..' , time.time()-t
  agt = agent.NeuralAgent(network,
                                  epsilon_start,
                                  epsilon_min,
                                  epsilon_decay,
                                  replay_memory_size,
                                  experiment_prefix,
                                  replay_start_size,
                                  update_frequency,
                                  rng)

  print 'agent done..'
  env = simulator.simulator()
  exp = experiment(agt,env)
  exp.run_episode(100)

launch()

