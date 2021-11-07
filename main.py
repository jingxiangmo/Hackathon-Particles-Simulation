from environment import *
from droplets import drops

numParticles = 100
numDroplets = 100


def noMask():
    # creates environment
    makeRoom()
    # creates person without mask
    makePerson(False)
    # sets number of particle
    setParticulesNumber(numParticles)
    # creates particles
    create_particles()
    # creates droplets
    drops(numDroplets)  # whats the percentage of droplets? Assume 1:1 for now
    # simulate particules movement
    collisionSimulation()


#
# =================== DIFFERENT COUGHING TYPES ==================== #
#
noMask()
# mask()
# n95Mask()
