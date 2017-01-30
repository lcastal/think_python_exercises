from __future__ import print_function, division
from chp10.inlist import build_list, bin_search

if __name__ == '__main__':
    t = build_list()

    for word in t:
        reverse_word = word[::-1]
        if bin_search(t, reverse_word):
            print("Pair found: ", word, reverse_word)
