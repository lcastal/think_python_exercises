import math


def fact(k):
    if k == 0:
        return 1
    else:
        return k*fact(k-1)


def estimate_pi():
    coefficient = 2 * math.sqrt(2) / 9801

    k=0
    result = 0.0

    while True:
        numerator = fact(4*k) * (1103+26390*k)
        denominator = fact(k)**4 * 396**(4*k)
        term = coefficient * numerator / denominator
        result += term

        if abs(term) < 1e-15:
            break
        k += 1

    return 1 / result


print("pi stimato: "+str(estimate_pi()))
print("math pi: "+str(math.pi))


