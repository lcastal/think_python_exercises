import math

def mysqtr(a):
    apx = 10 #approximation value
    y = a #start at same value
    while(apx):
        x = y
        y = (x + a/x) / 2
        apx -= 1
    return y


def test_square_root():
    print("a \t mysqrt(a) \t math.sqrt(a) \t diff")
    print("- \t --------  \t ------------ \t ----")
    a = 1
    while(a < 40):
        y1 = mysqtr(a)
        y2 = math.sqrt(a)
        diff = abs(y1 - y2)
        print("{0:d} \t {1:5f}  \t {2:5f} \t {3:5f}" .format(a, y1, y2, diff))
        a += 1


test_square_root()
