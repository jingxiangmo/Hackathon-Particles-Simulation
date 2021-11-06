from vpython import *

animation = canvas(width=800, height=400, align='left')
gray = color.gray(0.7)

animation.title = "COVID-19 Particles Simulation"
animation.caption = """
Right button or ctrl-drag to rotate camera
Shift-drag to pan left or right
Middle button or alt/option and drag to zoom
"""

# size of the box
d = 6
# radius of the container
r = 0.05

# box sized vectors
boxbottom = curve(color=gray, radius=r)
boxbottom.append([vector(-d, -d, -d), vector(-d, -d, d), vector(d, -d, d), vector(d, -d, -d), vector(-d, -d, -d)])
boxtop = curve(color=gray, radius=r)
boxtop.append([vector(-d, d, -d), vector(-d, d, d), vector(d, d, d), vector(d, d, -d), vector(-d, d, -d)])

# vertices of the boxes
vert1 = curve(color=gray, radius=r)
vert2 = curve(color=gray, radius=r)
vert3 = curve(color=gray, radius=r)
vert4 = curve(color=gray, radius=r)

vert1.append([vector(-d, -d, -d), vector(-d, d, -d)])
vert2.append([vector(-d, -d, d), vector(-d, d, d)])
vert3.append([vector(d, -d, d), vector(d, d, d)])
vert4.append([vector(d, -d, -d), vector(d, d, -d)])

#
# ================= Ball Example =================
#

ball = sphere(color=color.green, radius=0.1, retain=200)
ball.mass = 1.0
ball.p = vector(-0.15, -0.23, +0.27)

side = 4.0
thk = 0.3
s2 = 2 * side - thk
s3 = 2 * side + thk
side = side - thk * 0.5 - ball.radius

dt = 0.3
while True:
    rate(200)
    ball.pos = ball.pos + (ball.p / ball.mass) * dt
    if not (side > ball.pos.x > -side):
        ball.p.x = -ball.p.x
    if not (side > ball.pos.y > -side):
        ball.p.y = -ball.p.y
    if not (side > ball.pos.z > -side):
        ball.p.z = -ball.p.z
