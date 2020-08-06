#
# School of Continuing Studies, University of Toronto
# 3547 TERM PROJECT
# Intelligent Systems and Reinforcement Learning
# Robot obstacle avoidance with reinforcement learning
#
# Alexandre Dietrich
# Ankur Tyagi
# Haitham Alamri
# Rodolfo Vasconcelos
#

'''
Monte Carlo on-policy implementation.
4x4 Grid
'''


EPISODES = 1000 # number of episodes
MAX_EPISODE_STEPS = 200
GAMMA = 0.6
EPS = 0.4
ALL_POSSIBLE_ACTIONS = ('U', 'D', 'L', 'R')

"""## Imports"""

from builtins import range
import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict

"""## Print functions"""

def print_Q(Q, grid):
    print('----------------------------------------------')
    print('| State  | U      | D      | L      | R      |')
    print('----------------------------------------------')
    all_states = sorted(grid.all_states())
    for state in all_states:
        print("| {} |".format(state), end="")
        if state != (0,0) and state != (3,3):
            for action, value in Q[state].items():
                print(' {:>6.2f} |'.format(value), end="")
        else:
            print('   0.00 |   0.00 |   0.00 |   0.00 |',end="")
        print('')
    print('----------------------------------------------')

def print_values(V, g):
  for i in range(g.rows):
    print("---------------------------")
    for j in range(g.cols):
      v = V.get((i,j), 0)
      if v >= 0:
        print(" %.2f|" % v, end="")
      else:
        print("%.2f|" % v, end="") # -ve sign takes up an extra space
    print("")

def print_policy(P, g):
  for i in range(g.rows):
    print("---------------------------")
    for j in range(g.cols):
      a = P.get((i,j), ' ')
      print("  %s  |" % a, end="")
    print("")

"""## Grid World"""

class Grid: # Environment
  def __init__(self, rows, cols, start):
    self.rows = rows
    self.cols = cols
    self.i = start[0]
    self.j = start[1]

  def set(self, rewards, actions):
    # rewards should be a dict of: (i, j): r (row, col): reward
    # actions should be a dict of: (i, j): A (row, col): list of possible actions
    self.rewards = rewards
    self.actions = actions

  def set_state(self, s):
    self.i = s[0]
    self.j = s[1]

  def current_state(self):
    return (self.i, self.j)

  def is_terminal(self, s):
    return s not in self.actions

  
  def move(self, action):
    # check if legal move first
    #print('before i={} j={} action={}'.format(self.i,self.j,action))
    if action in self.actions[(self.i, self.j)]:
      if action == 'U':
        self.i -= 1
      elif action == 'D':
        self.i += 1
      elif action == 'R':
        self.j += 1
      elif action == 'L':
        self.j -= 1
    # return a reward (if any)
    #return self.rewards.get((self.i, self.j), 0)
    reward = self.rewards.get((self.i, self.j), 0)
    #print('after i={} j={} r={}'.format(self.i,self.j,reward))
    return reward

  def undo_move(self, action):
    # these are the opposite of what U/D/L/R should normally do
    if action == 'U':
      self.i += 1
    elif action == 'D':
      self.i -= 1
    elif action == 'R':
      self.j -= 1
    elif action == 'L':
      self.j += 1
    # raise an exception if we arrive somewhere we shouldn't be
    # should never happen
    assert(self.current_state() in self.all_states())

  def game_over(self):
    # returns true if game is over, else false
    # true if we are in a state where no actions are possible
    return (self.i, self.j) not in self.actions

  def all_states(self):
    # possibly buggy but simple way to get all states
    # either a position that has possible next actions
    # or a position that yields a reward
    return set(self.actions.keys()) | set(self.rewards.keys())


def standard_grid():
  # define a grid that describes the reward for arriving at each state
  # and possible actions at each state
  # the grid looks like this
  # S means start position
  # E means the end states
  #
  # E  .  .  .
  # .  .  . .
  # S  .  .  .
  # .  .  .  E
  g = Grid(4, 4, (2, 0))
#  rewards = {(3, 3): 0}
  rewards = {}
  actions = {
    #(0, 0): (), End-State
    (0, 0): ('D', 'R'),
    (0, 1): ('D', 'R', 'L'),
    (0, 2): ('D', 'R', 'L'),
    (0, 3): ('D', 'L'),
    (1, 0): ('D', 'R', 'U'),
    (1, 1): ('D', 'R', 'L', 'U'),
    (1, 2): ('D', 'R', 'L', 'U'),
    (1, 3): ('D', 'U', 'L'),
    (2, 0): ('D', 'U', 'R'),
    (2, 1): ('D', 'R', 'L', 'U'),
    (2, 2): ('D', 'R', 'L', 'U'),
    (2, 3): ('D', 'U', 'L'),
    (3, 0): ('U', 'R', ),
    (3, 1): ('U', 'R', 'L'),
    (3, 2): ('U', 'R', 'L'),
    (3, 3): ('U','L')
    #(3, 3): (), End-State
  }
  g.set(rewards, actions)
  return g

def update_rewards(grid, states, step_cost):
  for update_state in states:
    grid.rewards[update_state] = step_cost

def update_end_state(grid, state):
  grid.rewards[state] = 0
  grid.actions.pop(state)


def negative_grid(step_cost=-0.1):
  # in this game we want to try to minimize the number of moves
  # so we will penalize every move
  g = standard_grid()
  g.rewards.update({
    (0, 0): step_cost,
    (0, 1): step_cost,
    (0, 2): step_cost,
    (0, 3): step_cost,
    (1, 0): step_cost,
    (1, 1): step_cost,
    (1, 2): step_cost,
    (1, 3): step_cost,
    (2, 0): step_cost,
    (2, 1): step_cost,
    (2, 2): step_cost,
    (2, 3): step_cost,
    (3, 0): step_cost,
    (3, 1): step_cost,
    (3, 2): step_cost,
    (3, 3): step_cost,
  })
  return g

"""## pi functions"""

def max_dict(d):
  # returns the argmax (key) and max (value) from a dictionary
  # put this into a function since we are using it so often
  max_key = None
  max_val = float('-inf')
  for k, v in d.items():
    if v > max_val:
      max_val = v
      max_key = k
  return max_key, max_val


def policy_using_pi(St, pi):
    return np.random.choice(ALL_POSSIBLE_ACTIONS, p=[pi[(St,a)] for a in ALL_POSSIBLE_ACTIONS])

"""## Episode functions"""

def play_episode(grid, policy, pi):
  # returns a list of states and corresponding returns
  # in this version we will NOT use "exploring starts" method
  # instead we will explore using an epsilon-soft policy
  s = (2, 0)
  grid.set_state(s)
  a = policy_using_pi(s,pi)
  steps = 0


  # be aware of the timing
  # each triple is s(t), a(t), r(t)
  # but r(t) results from taking action a(t-1) from s(t-1) and landing in s(t)
  states_actions_rewards = [(s, a, 0)]
  while True:
    steps += 1
    r = grid.move(a)
    s = grid.current_state()
    if grid.game_over():
      states_actions_rewards.append((s, None, r))
      break
    else:
      a = policy_using_pi(s,pi)
      states_actions_rewards.append((s, a, r))
    if steps > MAX_EPISODE_STEPS:
      print(f"Monte Carlo took more than {MAX_EPISODE_STEPS} steps. It will be skipped.")
      break  

  # calculate the returns by working backwards from the terminal state
  G = 0
  states_actions_returns = []
  first = True
  for s, a, r in reversed(states_actions_rewards):
    # the value of the terminal state is 0 by definition
    # we should ignore the first state we encounter
    # and ignore the last G, which is meaningless since it doesn't correspond to any move
    if first:
      first = False
    else:
      states_actions_returns.append((s, a, G))
    G = r + GAMMA*G
  states_actions_returns.reverse() # we want it to be in order of state visited
  return states_actions_returns


"""## Run all episodes"""
def calculate_gridworld_policy(end_state=(3,3),obstable_list = []):
  # use the standard grid again (0 for every step) so that we can compare
  # to iterative policy evaluation
  # grid = standard_grid()
  # try the negative grid too, to see if agent will learn to go past the "bad spot"
  # in order to minimize number of steps
  grid = negative_grid(step_cost=-1)
  update_rewards(grid, obstable_list, -5)
  update_end_state(grid, end_state)

  # print rewards
  #print("rewards:")
  print_values(grid.rewards, grid)

  pi = defaultdict(lambda: 1/len(ALL_POSSIBLE_ACTIONS))  # probability of action (def random)

  # state -> action
  # initialize a random policy
  policy = {}
  for s in grid.actions.keys():
      policy[s] = np.random.choice(ALL_POSSIBLE_ACTIONS)

  # initialize Q(s,a) and returns
  Q = {}
  returns = {} # dictionary of state -> list of returns we've received
  states = grid.all_states()
  for s in states:
      if s in grid.actions: # not a terminal state
        Q[s] = {}
        for a in ALL_POSSIBLE_ACTIONS:
          Q[s][a] = -10
          returns[(s,a)] = []
  else:
      # terminal state or state we can't otherwise get to
      pass

  #print("initial Q:")
  #print_Q(Q,grid)

  # repeat until convergence
  deltas = []
  for t in range(EPISODES):
      #if t % 1000 == 0:
          #print(t)
          #print("Q:")
          #print_Q(Q,grid)

      # generate an episode using pi
      biggest_change = 0
      states_actions_returns = play_episode(grid, policy, pi)

      # calculate Q(s,a)
      seen_state_action_pairs = set()
      for s, a, G in states_actions_returns:
          # check if we have already seen s
          # called "first-visit" MC policy evaluation
          sa = (s, a)
          if sa not in seen_state_action_pairs:
              old_q = Q[s][a]
              returns[sa].append(G)
              Q[s][a] = np.mean(returns[sa])
              biggest_change = max(biggest_change, np.abs(old_q - Q[s][a]))
              seen_state_action_pairs.add(sa)
              A_star, _ = max_dict(Q[s])
              for a_index in ALL_POSSIBLE_ACTIONS:
                  if a_index == A_star:   pi[(s,a_index)] = 1 - EPS + EPS/len(ALL_POSSIBLE_ACTIONS)
                  else:                   pi[(s,a_index)] = EPS/len(ALL_POSSIBLE_ACTIONS)

      deltas.append(biggest_change)

      # calculate new policy pi(s) = argmax[a]{ Q(s,a) }
      for s in policy.keys():
          a, _ = max_dict(Q[s])
          policy[s] = a

  """## Print results"""

  #plt.plot(deltas)
  #plt.show()

  # find the optimal state-value function
  # V(s) = max[a]{ Q(s,a) }
  V = {}
  for s in policy.keys():
      V[s] = max_dict(Q[s])[1]

  #print("final values:")
  #print_values(V, grid)
  #print("final policy:")
  #print_policy(policy, grid)
  #print("final Q:")
  #print_Q(Q,grid)
  return policy


#print (f"returned policy={calculate_gridworld_policy((3,3),[(2,1)])}")
#print (f"returned policy={calculate_gridworld_policy((3,1),[(0,0)])}")
#print (f"returned policy={calculate_gridworld_policy((2,1),[(2,0),(0,0),(1,0)])}")

def print_policy_without_grid(P):
  grid = negative_grid(step_cost=-1)
  print_policy(P,grid)