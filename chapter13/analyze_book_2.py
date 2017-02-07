from analyze_book_1 import process_file


def subtract2(dict1, dict2):
    """
    Make the difference from the value of two dictionary
    :param dict1: dictionary
    :param dict2: dictionary
    :return: list
    """
    return set(dict1) - set(dict2)

def main():
    histogram_book = process_file("metamorphosis.txt")
    histogram_words = process_file("words.txt")

    result = subtract2(histogram_book, histogram_words)

    for key in result:
        print(key, end=" ")

if __name__ == "__main__":
    main()