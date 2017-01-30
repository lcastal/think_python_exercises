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


def check_metathesis(w1, w2, n):
    """
    Check if two anagrammed words have just n character swapped
    :param w1: string anagram of w2
    :param w2: string anagram of w1
    :param n: integer
    :return: boolean
    """
    count = 0

    if len(w1) != len(w2):
        return False

    for c1, c2 in zip(w1, w2):
        if c1 != c2:
            count += 1

    if count != n:
        return False
    else:
        return True


def find_metathesis(w, l, n):
    """
    Return a list of touples that contains all the metathesis word present in the list l
    :param w: string
    :param l: list
    :param n: integer
    :return: list
    """
    result = list()

    for elem in l:
        if check_metathesis(w, elem, n):
            result.append((w, elem))

    return result


def get_metathesis_list(l, n):
    """
    Take a list of lists and return a list of all couple metathesis words
    :param l: list
    :param n: integer
    :return: list of tuples
    """

    result = list()
    for sub_l in l:
        while len(sub_l) > 0:
            word = sub_l.pop()
            result += find_metathesis(word, sub_l, n)

    return result


if __name__  == "__main__":
    t = get_list_words("words.txt")
    d = dictionary_anagrams(t)

    t = get_metathesis_list(d.values(), 2)

    file_resutl = open("result.txt", "w")
    for elem in t:
        file_resutl.write(str(elem)+"\n")





