import turtle
from polygon import arc


def leave(t, r, degree):
    """ Print a petal

    :param t: Turtle istance
    :param r: radius of petal
    :param degree: of petal
    """
    for i in range(2):
        arc(t, r, degree)
        t.lt(180-degree)

def flower(t, n, r, degree):
    """ Print a flower

    :param t: Turtle istance
    :param n: number of petal
    :param r: the flower's radius
    :param degree: the size of flower
    """

    for i in range(n):
        leave(t, r, degree)
        t.lt(360/n)

def move(t, length):
    t.pu()
    t.fd(length)
    t.pd()


t = turtle.Turtle()

move(t,-200)
flower(t, 7, 60, 60.0)

move(t,200)
flower(t, 10, 40, 80.0)

move(t,200)
flower(t, 20, 140, 20.0)


turtle.mainloop()

