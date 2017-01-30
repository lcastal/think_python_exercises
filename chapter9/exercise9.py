def avoids(word, forbidden):
    for char in forbidden:
        if char in word:
            return False
    return True

def uses_only(word, permitted):
    for char in permitted:
        if char not in word:
            return False
    return True

def uses_all(word, all):
    return uses_only(word, all)

def isabecedarian(word):
    prev = 0
    for letter in word:
        if ord(letter) >= prev:
            prev = ord(letter)
        else:
            return False
    return True


while True:
    word = input("write a word (done for quit): ")
    if word == "done":
        print("Bye!")
        break

    elif isabecedarian(word):
        print("is abecedarian word!")

    else:
        print("is not abecedarian word!!!")