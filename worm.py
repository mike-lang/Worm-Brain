__author__ = 'Michael Lang'

import random
import math


# This should be revised when we've made firmer decisions on the nose sense modelling
def get_line(x1, y1, x2, y2):
    points = []
    issteep = abs(y2-y1) > abs(x2-x1)
    if issteep:
        x1, y1 = y1, x1
        x2, y2 = y2, x2
    rev = False
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
        rev = True
    deltax = x2 - x1
    deltay = abs(y2-y1)
    error = int(deltax / 2)
    y = y1
    ystep = None
    if y1 < y2:
        ystep = 1
    else:
        ystep = -1
    for x in range(int(x1), int(x2) + 1):
        if issteep:
            points.append((int(y), x))
        else:
            points.append((x, int(y)))
        error -= deltay
        if error < 0:
            y += ystep
            error += deltax
    # Reverse the list if the coordinates were reversed
    if rev:
        points.reverse()
    return points

def sniff_direction(loc_x, loc_y, direction, environment, sniff_distance):
    print 'Sniffing direction %s from location (%s, %s)).' % (direction, loc_x, loc_y)
    smell_end_x = loc_x + math.cos(direction) * sniff_distance
    smell_end_y = loc_y + math.sin(direction) * sniff_distance
    print 'Sniff input ends at location (%s, %s).' % (smell_end_x, smell_end_y)
    print 'Smelling contents of cells: '
    smelled_grid_cells = get_line(loc_x, loc_y, smell_end_x, smell_end_y)
    print smelled_grid_cells
    total_food = 0
    for cell in smelled_grid_cells:
        print 'Detecting food in (%s, %s) - %s' % (cell[0] % environment.width, cell[1] % environment.height, environment.food_density[cell[1] % environment.height][cell[0] % environment.width])
        total_food = total_food + environment.food_density[cell[1] % environment.height][cell[0] % environment.width]
    avg_food = total_food / len(smelled_grid_cells)

    # Calculate average food value and normalize against max possible
    print 'Normalized food density in direction %s : %s' % (direction, avg_food / environment.MAX_FOOD_DENSITY)
    return avg_food / environment.MAX_FOOD_DENSITY

class Worm(object):
    def __init__(self, environment):
        self.environment = environment
        self.brain = WormBrain()
        # Initialize position to a random location within the environment
        self.location_x = random.randint(0, environment.width)
        self.location_y = random.randint(0, environment.height)
        self.orientation = random.random() * 2 * math.pi
        # Initialize the worm to have 10 units of food energy
        self.energy_reserve = 10
        self.alive = True
    # Here I model the worm's external sensory organ as a mapping from environment + worm position/orientation to
    # value(s) to feed into the decision making apparatus.  I call it smell because it detects food and its not
    # optical.  Lets start by generating 3 values, each one corresponding to the food density in the environment along
    # a particular line originating from the worm
    def smell_environment(self):
        sensory_distance = 5
        center_nostril_direction = self.orientation
        left_nostril_direction = self.orientation + ((15 / 360) * 2 * math.pi)
        right_nostril_direction = self.orientation + ((15 / 360) * 2 * math.pi)
        left_nostril_excitation = sniff_direction(self.location_x, self.location_y, left_nostril_direction, self.environment, sensory_distance)
        center_nostril_excitation = sniff_direction(self.location_x, self.location_y, center_nostril_direction, self.environment, sensory_distance)
        right_nostril_excitation = sniff_direction(self.location_x, self.location_y, right_nostril_direction, self.environment, sensory_distance)
        nose_excitation = (left_nostril_excitation, center_nostril_excitation, right_nostril_excitation)
        print nose_excitation
        return nose_excitation
    def consume_food(self):
        food_present = self.environment.food_density[int(self.location_y)][int(self.location_x)]
        print 'Consuming %s units of food from current location (%s, %s) ' % (food_present, self.location_x, self.location_y)
        self.energy_reserve = self.energy_reserve + food_present
        self.environment.food_density[int(self.location_y)][int(self.location_x)] = 0
    def metabolize_food(self):
        self.energy_reserve = self.energy_reserve - 1
        if self.energy_reserve < 0:
            # worm starved to death. :(
            self.alive = False
    # A step in the life of a worm:
    def live(self):
        self.consume_food()
        self.metabolize_food()

        if not self.alive:
            return

        nose_sense_data = self.smell_environment()
        motor_neuron_excitations = self.brain.deliberateOnSenseData(nose_sense_data)
        # do stuff based upon motor neuron excitations here - perhaps dispatch the excitations of motor organ objects ???
    def print_worm_state(self):
        print('I\'m a worm!  A textual rendering of my state goes here!')

class WormBrain(object):
    def __init__(self):
        # initialize whatever structure from heredity/connectome here
        pass
    def deliberateOnSenseData(self, nose_sense_data):
        # Return a vector of motor neuron excitations, for body to process and generate actions from
        pass

