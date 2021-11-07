from environment import *
from droplets import drops

numParticles = 100
numDroplets = 100


##########################################################

# When you do the masks, reduce the vx of the droplets
# Might want to make the droplets fall slower (idk how to)

##########################################################


def noMask():
    probability = 1

    # creates environment
    makeRoom()
    # creates person without mask
    makePerson(False)
    # sets number of particle
    setParticulesNumber(numParticles, probability)
    # creates particles
    create_particles()
    # creates droplets
    drops(numDroplets, probability)  # whats the percentage of droplets? Assume 1:1 for now
    # simulate particules movement
    collisionSimulation()


def normalMask():
    probability = 0.5

    # creates environment
    makeRoom()
    # creates person without mask
    makePerson(True)
    # sets number of particle
    setParticulesNumber(numParticles, probability)
    # creates particles
    create_particles()
    # creates droplets
    drops(numDroplets, probability)  # whats the percentage of droplets? Assume 1:1 for now
    # simulate particules movement
    collisionSimulation()


def n95Mask():
    # change number of particles to 0.95% of the total
    probability = 0.05

    # creates environment
    makeRoom()
    # creates person without mask
    makePerson(True)
    # sets number of particle
    # p as in percentage of particles passed through
    setParticulesNumber(numParticles, probability)
    # creates particles
    create_particles()
    # creates droplets
    drops(numDroplets, probability)  # whats the percentage of droplets? Assume 1:1 for now
    # simulate particules movement
    collisionSimulation()


#
# =================== DIFFERENT COUGHING TYPES ==================== #
#

case = input("Enter case (1-3): ")
if case == "1":
    noMask()
elif case == "2":
    normalMask()
elif case == "3":
    n95Mask()
else:
    print("please input a valid number")
