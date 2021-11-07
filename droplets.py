from vpython import *
import random


# num = 100


def drops(num):
    # create droplets
    droplets = []

    # create the droplets
    for i in range(num):
        droplets.append(sphere(radius=0.05, pos=vector(-5, 0.0001, 0), color=color.cyan,
                               make_trail=True, retain=5, trail_radius=0.001))

    # Basic physics variables
    t = 0
    dt = 5
    dtz = 50
    g = 9.8
    # speed
    vy = 0.15
    vx = 0.3
    vz = 0.01

    switch = 0
    # simulate
    while switch != 1:
        rate(100)

        ay = -g
        for i in range(num):
            constx = droplets[i].pos.x
            consty = droplets[i].pos.y
            # change the position and the random direction
            droplets[i].pos.x += vx * dt * random.uniform(0, 2)
            droplets[i].pos.y += vy * dt * random.uniform(0, 1)
            droplets[i].pos.z += vz * dtz * \
                random.uniform(0, 2) * random.randint(-1, 1)
            if abs(droplets[i].pos.y) >= 6:
                # stale droplet
                droplets[i].pos.y = -6
                droplets[i].pos.x = constx
                droplets[i].pos.z = consty
            if droplets[num - 1].pos.y == 0:
                switch += 1
        vy += ay / 100 * dt
        t += dt
