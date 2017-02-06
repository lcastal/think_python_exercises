import string


def file_to_list(path):
    """
    The function read the content of a file and return the content in a list
    :param path: file's path
    :return: list
    """
    try:
        fd = open(path)
    except:
        return 0

    result = list()
    for line in fd:
        if line == "\n":
            continue
        result += line_to_list(line)

    return result


def line_to_list(line):
    """
    Take a string and split all the word in the string
    :param line: string
    :return: list
    """

    result = list()
    line = clean_line(line)

    line_splitted = line.split(" ")

    return line_splitted


def clean_line(line):
    """
    Remove all special caracter in the line, al line only the space
    :param line: string
    :return: string
    """
    line.strip()
    line = line.lower()

    # take off gerundium
    line = line.replace("'s", "")
    line = line.replace("--", " ")

    # take off special characters
    string_special_char = string.punctuation+string.whitespace[1:]
    d_table = dict(zip(string_special_char, [""]*len(string_special_char)))
    table = str.maketrans(d_table)

    line = line.translate(table)

    return line


def make_dict_frequency(l):
    """
    Take a list and create a dictionary as follow {key : word, value : frequency}
    :param l: list of word
    :return: dictionary
    """
    d = dict()
    for word in l:
        d[word] = d.get(word, 0) + 1
    return d


def build_histogram_text(path_source, path_result):
    """
    Take a file text and write a file path_result with the counting of all words
    :param path_source: source text
    :param path_result: result text
    :return:
    """
    l = file_to_list(path_source)

    total_number_words = len(l)
    d = make_dict_frequency(l)
    #build a list sorted
    l = sorted(d.items(), key=lambda x: x[1], reverse=True)

    fd = open(path_result, "w")

    fd.writelines("Total words: "+str(total_number_words)+"\n")
    for key, value in l:
        fd.write("word: "+key+" frequency: "+str(value)+"\n")


if __name__ == "__main__":
    build_histogram_text("pride_and_prejudice.txt", "histogram_pride_and_prejudice.txt")
    build_histogram_text("adventures_huckleberry_finn.txt", "histogram_adventures_huckleberry_finn.txt")
    build_histogram_text("alice_adventures.txt", "histogram_alice_adventures.txt")
    build_histogram_text("metamorphosis.txt", "histogram_metamorphosis.txt")

