from vpython import *
import random

num = 100

droplets = []

for i in range(num):
    droplets.append(sphere(radius=0.5, pos=vector(-5, 3, 0), make_trail=True, retain=100, trail_radius=0.03))

t = 0
dt = 0.1
g = 9.8

# speed
vy = 1 
vx = 1
vz = 1

while droplets[0].pos.y > 0:
    rate(200)

    ay = -g
    for i in range(num):
        droplets[i].pos.x += vx * dt * random.uniform(0, 2)
        droplets[i].pos.y += vy * dt * random.uniform(0, 2)
        droplets[i].pos.z += vz * dt * random.uniform(0, 2)

    vy += ay / 100 * dt
    t += dt