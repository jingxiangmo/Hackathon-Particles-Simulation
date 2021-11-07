from environment import *
from droplets import drops

numParticles = 100
numDroplets = 100


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
    drops(numDroplets, probability, 1)  # whats the percentage of droplets? Assume 1:1 for now
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
    drops(numDroplets, probability, 0.7)  # whats the percentage of droplets? Assume 1:1 for now
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
    drops(numDroplets, probability, 0.5)  # whats the percentage of droplets? Assume 1:1 for now
    # simulate particules movement
    collisionSimulation()


#
# =================== DIFFERENT COUGHING TYPES ==================== #
#

case = input("Enter case (no_mask, medical_mask, n95_mask): ")
if case == "no_mask":
    noMask()
elif case == "medical_mask":
    normalMask()
elif case == "n95_mask":
    n95Mask()
else:
    print("please input a valid number")
