def do_twice(f):
    f()
    f()

def do_four(f):
    do_twice(f)
    do_twice(f)

def one_four_one(f, g, h):
    f()
    do_four(g)
    h()

def print_plus():
    print("+", end=" ")

def print_minus():
    print("-", end=" ")

def print_pipe():
    print("|", end=" ")

def print_blank():
    print(" ", end=" ")

def print_nothing():
    print("", end="")

def print_end():
    print()

def print1beam():
    one_four_one(print_nothing, print_minus, print_plus)

def print1post():
    one_four_one(print_nothing, print_blank, print_pipe)

def print4beams():
    one_four_one(print_plus, print1beam, print_end)

def print4posts():
    one_four_one(print_pipe, print1post, print_end)

def print_row():
    one_four_one(print_nothing, print4posts, print4beams)

def print_grid():
    one_four_one(print4beams, print_row, print_nothing)

print_grid()

