from environment import *
from droplets import drops

numParticles = 100
numDroplets = 100
##########################################################

# When you do the masks, reduce the vx of the droplets
# Might want to make the droplets fall slower (idk how to)

##########################################################


def noMask():
    # creates environment
    makeRoom()
    # creates person without mask
    makePerson(False, None)
    # sets number of particle
    setParticulesNumber(numParticles)
    # creates particles
    create_particles()
    # creates droplets
    drops(numDroplets)  # whats the percentage of droplets? Assume 1:1 for now
    # simulate particules movement
    collisionSimulation()


def n95Mask():
    # creates environment
    makeRoom()
    # creates person without mask
    makePerson(True)
    # sets number of particle
    setParticulesNumber(numParticles)
    # creates particles
    create_particles()
    # creates droplets
    drops(numDroplets)  # whats the percentage of droplets? Assume 1:1 for now
    # simulate particules movement
    collisionSimulation()

# def normalMask():
#     # creates environment
#     makeRoom()
#     # creates person without mask
#     makePerson(True)
#     # sets number of particle
#     setParticulesNumber(numParticles)
#     # creates particles
#     create_particles()
#     # creates droplets
#     drops(numDroplets)  # whats the percentage of droplets? Assume 1:1 for now
#     # simulate particules movement
#     collisionSimulation()


#
# =================== DIFFERENT COUGHING TYPES ==================== #
#
n95Mask()
# normalMask()
# noMask()
