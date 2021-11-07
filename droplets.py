from vpython import *
import random

#num = 100


def drops(num):
    # create droplets
    droplets = []

    # create the droplets
    for i in range(num):
        droplets.append(sphere(radius=0.01, pos=vector(-5, 0.0001, 0), color=color.cyan,
                        make_trail=True, retain=50, trail_radius=0.001))

    # Basic physics variables
    t = 0
    dt = 0.1
    g = 9.8
    # speed
    vy = 1
    vx = 1
    vz = 1

    # simulate
    while droplets[0].pos.y > 0:
        rate(200)

        ay = -g
        for i in range(num):
            # change the position and the random direction
            droplets[i].pos.x += vx * dt * random.uniform(0, 2)
            droplets[i].pos.y += vy * dt * random.uniform(0, 2)
            droplets[i].pos.z += vz * dt * random.uniform(0, 2)

        vy += ay / 100 * dt
        t += dt
