from __future__ import print_function, division
import string, random


def process_file(path):
    """
    The function read the content of a file and return the content in a dict
    :param path: file's path
    :return: dict
    """
    fd = open(path)
    histogram = dict()

    for line in fd:
        process_line(line, histogram)

    return histogram


def process_line(line, histogram):
    """
    Take a string and split all the word and added in a dictionary
    :param line: string
    :param histogram: dictionary
    """

    line = line.replace("--", " ")
    for word in line.split():
        word = word.strip(string.punctuation+string.whitespace)
        word = word.lower()
        histogram[word] = histogram.get(word, 0) + 1


def most_common(histogram):
    """
    Return a list with frequency sorted
    :param histogram: dictionary
    :return: list
    """
    t = list()
    t = sorted(histogram.items(), key=lambda x: x[1], reverse=True)
    return t


def print_most_common(histogram, num=10):
    t = most_common(histogram)
    for word, freq in t[:num]:
        print(word, freq, sep="\t")


def total_words(histogram):
    """
    Return the number of words used in the text
    :param histogram: dictionary
    :return: intefer
    """
    return sum(histogram.values())


def different_words(histogram):
    """
    Return the number of different words used in the text
    :param histogram: dictionary
    :return: integer
    """
    return len(histogram)


def main():
    biblioteque = ["pride_and_prejudice.txt",
                 "adventures_huckleberry_finn.txt",
                 "alice_adventures.txt",
                 "metamorphosis.txt"]

    for book in biblioteque:
        histogram = process_file(book)
        sum_words = total_words(histogram)
        print("Total number words: %d" %(sum_words))
        print_most_common(histogram, 5)


if __name__ == "__main__":
    main()
