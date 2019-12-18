# epsilon-greedy example implementation of a multi-armed bandit
import random

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

import simulator
import reference_bandit

# generic epsilon-greedy bandit
class Bandit:
    
    def reset(self, epsilon=0.1):
        self.epsilon = epsilon
        self.frequencies = [0] * len(arms)
        self.sums = [0] * len(arms)
        self.expected_values = [0] * len(arms)
        self.iteration = 0
    
    def __init__(self, arms, epsilon=0.1, x=0.992, resetIterations=1000):
        print("INIT!")
        self.resetIterations = resetIterations
        self.arms = arms
        self.x = x
        self.reset()

    def run(self):
        if self.iteration == self.resetIterations:
            self.reset()
        
        self.iteration = self.iteration + 1
        
        if min(self.frequencies) == 0:
            return self.arms[self.frequencies.index(min(self.frequencies))]
        if random.random() < self.epsilon: 
            return self.arms[random.randint(0, len(arms) - 1)]
        return self.arms[self.expected_values.index(max(self.expected_values))]

    def give_feedback(self, arm, reward):
        arm_index = self.arms.index(arm)
        sum = self.sums[arm_index] + reward
        self.sums[arm_index] = sum
        frequency = self.frequencies[arm_index] + 1
        self.frequencies[arm_index] = frequency
        expected_value = sum / frequency
        self.expected_values[arm_index] = expected_value
        self.epsilon = self.epsilon * self.x

# configuration
arms = [
    'Configuration a',
    'Configuration b',
    'Configuration c',
    'Configuration d',
    'Configuration e',
    'Configuration f'
]

# instantiate bandits
bandit = Bandit(arms)
ref_bandit = reference_bandit.ReferenceBandit(arms)

