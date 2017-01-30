'''
english
spanish
german
french
italian
'''


def most_frequent(word):
    """
    Takes a word and resturn a list of letter in discending order based on its frequency
    :param word: string
    :return: list of character
    """
    d_freq = dict()

    #count the frequence of the words
    for letter in word:
        d_freq[letter] = 1 + d_freq.get(letter, 0)

    #create a list of tuples (frequence, letter)
    v = list()
    for letter, frequence in d_freq.items():
        v.append( (frequence, letter) )

    v.sort(reverse=True)

    #create a list of the letter in descending frequency
    result = list()
    for frequence, letter in v:
        result.append(letter)

    return result


def read_file(filename):
    """Returns the contents of a file as a string."""
    return open(filename).read()


if __name__ == "main":
    words = read_file("file_name")
    list_frequency = most_frequent(words)
    for elem in list_frequency:
        print(elem)


t = most_frequent("cisonopochepersonelaggiu")
print(t)
