def clean_words(t):
    """
    Remove junke character from the string present in the list
    :param t: list of string
    :return: list of cleaned string
    """
    l = list()
    for elem in t:
        l.append(elem.strip())

    return l


def get_list_words(file_name):
    """
    Takes a file name and return a list of line present in the file
    :param file_name: file's path
    :return: list of line
    """
    fin = open(file_name)
    return clean_words(list(fin))


def dictionary_anagrams(t):
    """
    Take a list of word and return a dictionary composed in this way:
    { key = 'tuples o letters' : [list of all the words composed by the letter's key present in the list t]
    :param t: list of words
    :return: dictionary
    """

    d = dict()
    for elem in t:
        key_tuple = tuple(sorted(list(elem)))
        if key_tuple in d:
            d[key_tuple] += [elem]
        else:
            d[key_tuple] = [elem]
    return d



t = get_list_words("words.txt")
d = dictionary_anagrams(t)

result = list()
for key, l in d.items():
    print(l)
    result.append(l)
