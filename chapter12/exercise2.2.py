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


def get_sortet_list(d):
    """
    Get a dictionary and return a list of value ordered based on it lenght
    :param d: dictionary {key:list}
    :return: list of list
    """

    # dictionary key=lenght of list anagram, value = list of lists
    d_key_lenght = dict()
    for key, value in d.items():
        if len(value) in d_key_lenght.keys():
            d_key_lenght[len(value)].append(value)
        else:
            d_key_lenght[len(value)] = [value]

    result = list()

    # sort the keys (number of word anagram) in decreasing order
    keys = list(d_key_lenght.keys())
    keys.sort(reverse=True)

    for key in keys:
        for elem in d_key_lenght[key]:
            result.append(elem)

    return result


t = get_list_words("words.txt")
d = dictionary_anagrams(t)
t = get_sortet_list(d)

file_resutl = open("result.txt", "w")
for elem in t:
    file_resutl.write("len: "+str(len(elem))+"content: "+str(elem)+"\n")
