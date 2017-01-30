from __future__ import print_function, division
from chp10.inlist import build_list, bin_search


def recursive_build_list(w, t, s):
    """
    Recursively build a list of all possible interlocked words based on t and s
    :param w: string
    :param t: list
    :param s: list
    :return: list
    """
    if len(t) == 0 and len(s) == 0:
        return [w]

    elif len(t) > 0 and len(s) > 0:
        return recursive_build_list(w+s[0], t, s[1:]) + recursive_build_list(w+t[0], t[1:], s)

    elif len(t) == 0:
        return recursive_build_list(w+s[0], t, s[1:])

    else:
        return recursive_build_list(w+t[0], t[1:], s)


def merge_words(w, z):
    """
    Build a list of words interlocked based on w and z
    :param w: string
    :param z: string
    :return: list
    """

    list_w = list(w)
    list_z = list(z)

    return recursive_build_list("", list_w, list_z)


if __name__ == '__main__':
    t = merge_words("shoe", "cold")

    z = build_list()
    for word in t:
        if bin_search(z, word):
            print("Interlocked word founded: ", word)



