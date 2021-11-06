def person(a, b, c):
    """
    vector(a, b, c)
    model of a person
    """
    head = sphere(pos=vector(a, b, c), color=color.gray(.6), radius=0.6)
    body = box(pos=vector(1, b - 1.5, c), size=vector(2, 1, 1), color=vector(0.72, 0.42, 0), axis=vector(0, 1, 0))
    compound([body, head])


a = 1
b = 2
c = 1
person(a, b, c)
