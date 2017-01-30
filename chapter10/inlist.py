from __future__ import print_function, division


def build_list():
    file_reader = open("words.txt")
    file_list = []

    for line in file_reader:
        file_list.append(line.strip())

    file_reader.close()
    return file_list


def bin_search(t, w):
    size_list = len(t)

    if size_list == 1:
        return t[0] == w

    index_search = size_list//2

    if w >= t[index_search]:
        return bin_search(t[index_search:], w)

    else:
        return bin_search(t[:index_search], w)


if __name__ == '__main__':
    word_list = build_list()

    for word in ['aa', 'alien', 'allen', 'zymurgy']:
        print(word, 'in list', bin_search(word_list, word))


