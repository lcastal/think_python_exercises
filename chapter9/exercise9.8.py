def is_palindromic(word):
    """
    Verify is a word is palindromic

    :param word: the word to check

    :return True if is palindromic, False otherwise
    """
    i, j = 0, len(word)-1
    while i < j:
        if word[i] != word[j]:
            return False
        i += 1
        j -= 1
    return True


def find_palindromic_sequence():
    i = 0
    while i < 1000000:
        sequence_temp = "%06d" %i
        if is_palindromic(sequence_temp[2:]):
            sequence_temp2 = "%06d" %(i+1)
            sequence_temp3 = "%06d" %(i+2)
            sequence_temp4 = "%06d" %(i+3)

            if is_palindromic(sequence_temp2[1:]) and is_palindromic(sequence_temp3[1:5])and is_palindromic(sequence_temp4):
               print("%06d" %i)
        i +=1

if __name__ == '__main__':
    find_palindromic_sequence()