def is_reverse(a, b):
    """
    :param a: string
    :param b: string
    :return: True if a is equal to reverse of b, False otherwise
    """

    if len(a) != len(b):
        return False
    b_reversed = ""
    for char in b:
        b_reversed = char + b_reversed

    if a == b_reversed:
        return True
    else:
        return False

def find_age():
    for i in range(1, 99):
        count = 0
        for j in range(0, 99):
            mother = str(i+j).zfill(2)
            child = str(j).zfill(2)
            if is_reverse(mother, child):
                count += 1
        if count > 7:
            print("mother - child")
            for j in range(0, 99):
                mother = str(i+j).zfill(2)
                child = str(j).zfill(2)
                if is_reverse(mother, child):
                    print(mother+" "+child)


if __name__ == '__main__':
    find_age()