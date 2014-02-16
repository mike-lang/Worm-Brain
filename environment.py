__author__ = 'Michael Lang'

import random

class Environment(object):
    MAX_FOOD_DENSITY = 5
    def __init__(self, environment_size_x, environment_size_y):
        self.width = environment_size_x
        self.height = environment_size_y
        # Not sure what kind of controls we want to use here.
        # Same environment for each iteration?
        # Same total quantity of food, with random distribution?
        # Wholly random food quantity and distribution?
        # For now, since its especially simply to implement, we'll just initialize the entire environment
        # randomly.  Each square in the grid gets a random float somewhere in [0, MAX_FOOD_DENSITY)
        self.food_density = []
        for j in range(self.height):
            line = []
            for j in range(self.width):
                line.append(random.random() * Environment.MAX_FOOD_DENSITY)
            self.food_density.append(line)
    def print_environment(self):
        for line in self.food_density:
            print line





