import random, string


def markov_analysis(text_list, num_pre=2):
    """
    List of word, and numbers of word for build a prefix
    :param text_list: list
    :param num_pre: int
    :return: dictionary
    """
    dictionary = dict()
    for i in range(len(text_list) - num_pre):

        prefix = tuple(text_list[i: i+num_pre])
        suffix = text_list[i+num_pre]

        if dictionary.get(prefix, 0) != 0:
            dictionary[prefix].append(suffix)
        else:
            dictionary[prefix] = [suffix]

    return dictionary


def get_random_text (dictionary, n=100):
    """
    Based on a dictionary build by markov analysis returns a random text
    :param dictionary: key=prefix value=all possible word after prefix
    :param n: lenght of random text
    :return: string
    """
    prefix_list = list(dictionary.keys())
    _prefix = random.choice(prefix_list)

    random_text = " ".join(_prefix)+" "
    for i in range(n-len(_prefix)-1):
        try:
            random_string = get_random_string(dictionary.get(_prefix))
        except:
            get_random_text (dictionary, n-i)

        random_text += random_string + " "
        _prefix = tuple(list(_prefix[1:]) + [random_string])


    return random_text


def get_random_string(t):
    """
    Get a random value from a list t
    :param t: list
    :return: string
    """
    return t[random.randint(0, len(t)-1)]


def file_to_list(path):
    """
    Take a file and return a list that contain all the word
    :param path: string
    :return: list
    """
    fd = open(path)
    t = list()
    for line in fd:
        t += process_line(line)

    return t


def process_line(line):
    """
    Take a string and split all the word and added in a list
    :param line: string
    """
    t = list()
    line = line.replace("--", " ")
    for word in line.split():
        word = word.strip(string.punctuation+string.whitespace)
        word = word.lower()
        t.append(word)

    return t


def main():
    t = file_to_list("metamorphosis.txt")
    markov_dictionary = markov_analysis(t, 4)

    fd = open("dictionary.txt", "w")
    fd.write(str(markov_dictionary))

    random_text = get_random_text(markov_dictionary)
    print(len(random_text.split(" ")))
    print(random_text)


if __name__ == "__main__":
    main()