import gym
from gym import error, spaces, utils
from gym.utils import seeding

import numpy as np

class GridJump(gym.Env):
  metadata = {'render.modes': ['human']}
  def __init__(self):
    self.grid = np.zeros((5, 5))
    self.states = np.arange(0, 25)
    self.special_states = { 1 : (10, 21), 3: (5, 13) }

    self.left_edge_states = [5, 10, 15]
    self.right_edge_states = [9, 14, 19]
    
    self.actions = [0, 1, 2, 3] #up, right, down, left
    
    self.reward_norm = 0
    self.reward_off = -1
    self.last_state = 0
  
  def get_next_state(self, action):
    if action == 0:
      state = self.last_state - 5
    elif action == 1:
      state = self.last_state + 1
    elif action == 2:
      state = self.last_state + 5
    elif action == 3:
      state = self.last_state - 1

    return state

  def setState(self, state):
    self.last_state = state

  def step(self, action):
    reward = 0
    # print("step", self.last_state, "action", action)
    if self.last_state in [int(i) for i in list(self.special_states.keys())]:
      # print("special")
      reward, state = self.special_states[self.last_state]
      # self.last_state = state
      return reward, state
    
    if ((self.last_state in self.left_edge_states) and (action == 3)) or ((self.last_state in self.right_edge_states) and (action == 1)):
      # print("edge")
      
      reward = -1
      return reward, self.last_state

    next_state = self.get_next_state(action)

    if (next_state < 0) or (next_state > 24):
      # print("outside")
      reward = -1
      return reward, self.last_state

    # print("move")
    # self.last_state = next_state
    return reward, next_state
    
    
  def reset(self):
    self.last_state = 0

  def render(self, mode='human'):
    return

  def close(self):
    return

  def getStates(self):
    return self.states

  def getActions(self):
    return self.actions

  


  

  