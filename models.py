from vpython import *


def person(x, y, z):
    """
    vector(a, b, c)
    model of a person
    """
    head = sphere(pos=vector(x, y, z), color=color.gray(.6), radius=0.6)
    body = box(pos=vector(x, y - 1.5, z), size=vector(2, 1, 1),
               color=vector(0.72, 0.42, 0), axis=vector(0, 1, 0))
    compound([body, head])
