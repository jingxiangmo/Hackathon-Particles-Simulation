from vpython import *
from random import *

droplets = []
NAtoms = 1

for i in range(NAtoms):
    droplets.append(sphere(radius = 0.03, pos = vector(-5, 3, 0)))
    t = 0
    dt = 0.1
    g = 9.8
    vy= 2
    vx= 2

for droplet in droplets:
    rate(50)
    ay = -g
    droplet.pos.x += vx * dt
    droplet.pos.y += vy * dt
    vy += ay/100 * dt
    t += dt
