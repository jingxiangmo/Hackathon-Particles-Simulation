from vpython import *

droplet = sphere(radius = 1, pos = vector(-5, 3, 0))
t = 0
dt = 0.1
g = 9.8
vy= 2
vx= 2

while droplet.pos.y > 0:
    rate(100)
    ay = -g
    droplet.pos.x += vx * dt
    droplet.pos.y += vy * dt
    vy += ay/100 * dt
    t += dt
