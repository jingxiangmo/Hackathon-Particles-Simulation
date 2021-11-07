from vpython import *
import random

# PROBLEMS:
# 2. The droplets should spread randomly on z axis
# 3. The droplets should be launched at the same time
# 4. The droplets should disappear


# MAKE THE PARTICLES DISAPPEAR WHEN <-6
def drops(num):
    # create droplets
    droplets = []

    # create the droplets
    for i in range(num):
        droplets.append(
            sphere(radius=0.03, pos=vector(-5, 0.0001, 0), color=color.cyan, make_trail=True, retain=5, trail_radius=0.001))

    # Basic physics variables
    t = 0
    dt = 0.1
    g = 9.8
    # speed, RANDOMIZE
    vy = 0.15
    vx = 0.5
    vz = 0.05

    # simulate
    while droplets[0].pos.y > -6:
        rate(200)

        ay = -g
        for i in range(num):
            # change the position and the random direction
            droplets[i].pos.x += vx * dt * random.uniform(0, 2)
            droplets[i].pos.y += vy * dt * random.uniform(0, 2)
            droplets[i].pos.z += vz * dt * random.uniform(0, 2)

        vy += ay / 100 * dt
        t += dt
