



def is_triple_word(word):
    count = 0
    i = 0
    while i < len(word)-1:
        if word[i] == word[i-1]:
            count = count +1
            if count == 3:
                return True
            i = i+2
        else:
            count = 0
            i = i + 1
    return False


def find_triple_word():
    fin = open("words.txt")
    for line in fin:
        word = line.strip()
        if is_triple_word(word):
            print(word)

find_triple_word()




