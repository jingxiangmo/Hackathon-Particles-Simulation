from vpython import *
import random


# num = 100


def drops(num, probability, velocity_range):
    # probability of droplets being created
    num = int(num * probability)

    # create droplets
    droplets = []

    # create the droplets
    for i in range(num):
        droplets.append(
            sphere(radius=random.gauss(0.07, 0.01), pos=vector(-4.4, 0.0001, 0), color=color.cyan, make_trail=True,
                   retain=5, trail_radius=0.001))

    # Basic physics variables
    t = 0
    dt = 5
    dtz = 50
    g = 9.8
    # speed
    vy = 0.3
    vx = 0.3 * velocity_range
    vz = 0.01

    switch = 0
    # simulate
    while droplets[0].pos.y > -11:
        rate(1)
        ay = -g
        for i in range(num):
            # change the position and the random direction
            droplets[i].pos.x += vx * dt * random.uniform(0, 2)
            droplets[i].pos.y += vy * dt * random.uniform(0, 1)
            droplets[i].pos.z += vz * dtz * \
                                 random.uniform(0, 2) * random.randint(-1, 1)
            if abs(droplets[i].pos.y) > 6:
                # delete the droplet if below ground
                droplets[i].visible = False
        vy += ay / 100 * dt
        t += dt
