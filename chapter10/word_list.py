import time


def build_list_append():
    file_reader = open("words.txt")
    file_list = []

    for line in file_reader:
        file_list.append(line.strip())

    file_reader.close()
    return file_list


def build_list_plus():
    file_reader = open("words.txt")
    file_list = []

    for line in file_reader:
        file_list += [line.strip()]

    file_reader.close()
    return file_list


if __name__ == '__main__':
    tx = time.time()
    t = build_list_append()
    ty = time.time()

    time_result = ty-tx
    print("Tempo build list append: %f" % time_result)
    print("Numbers of elements in list: %d" % len(t))

    tx = time.time()
    t = build_list_append()
    ty = time.time()

    time_result = ty-tx
    print("Tempo build list plus: %f" % time_result)
    print("Numbers of elements in list: %d" % len(t))


