__author__ = 'Michael Lang'

from worm import Worm
from environment import Environment

class Simulation(object):
    def __init__(self, environmentSizeX, environmentSizeY):
        self.environment = Environment(environmentSizeX, environmentSizeY)
        self.worm = Worm(self.environment)
        self.clock = 0
    def executeTimeStep(self):
        print 'Time Step: %s' % self.clock
        self.render_display()
        self.worm.live()
        if not self.worm.alive:
            # worm is dead.  Return value to signal simulation is done
            return False
        self.clock = self.clock + 1
    def render_display(self):
        self.environment.print_environment()
        self.worm.print_worm_state()



the_simulation = Simulation(50, 50)

# To start testing this thing, run for at most X steps
while the_simulation.clock < 5:
    the_simulation.executeTimeStep()