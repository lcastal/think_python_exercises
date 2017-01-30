import turtle, math


def polyline(t, n, length, angle):
    """Generic function that print a fraction of a circle

    :param t: a Turtle istance
    :param n: number of segment
    :param length: the lenght of each segment
    :param angle: fraction to print

    """
    for i in range(n):
        t.fd(length)
        t.lt(angle)


def square(t, length): # encapsulation; generalization
    """ Print a square

    :param t: a Turtle istance
    :param length: the size of each side

    """
    for i in range(4):
        t.fd(length)
        t.lt(90)


def polygon(t, length, n): # generalization
    """Print a polygon

    :param t: a Turtle istance
    :param length: size of each segment
    :param n: the segment number
    """
    angle = 360 / n

    polyline(t, n, length, angle)


def circle(t, r): # design interface
    """Print a circle

    :param t: a Turtle istance
    :param r: the radius length

    """
    arc(t, r, 360.0)


def arc(t, r, angle):
    """Print a segment of a circumference

    :param t: a Turtle istance
    :param r: the radius
    :param angle: fraction to print

    """
    arc_length = math.pi * 2 * r * angle / 360
    n = int(arc_length/3) + 1
    step_length = arc_length / n
    step_angle = angle / n

    polyline(t, n, step_length, step_angle)

if __name__ == '__main__':
    bob = turtle.Turtle()

    square(bob, 200)
    polygon(bob, 100, 9)
    circle(bob, 80)
    arc(bob, 100, 270)

    turtle.mainloop()