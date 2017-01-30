

def avoid(word, chars):
    for char in chars:
        if char in word:
            return False
    return True

while True:
    word = input("parola: ")
    if word == "done":
        break

    chars = input("caratteri proibiti: ")
    result = avoid(word, chars)
    if result:
        print("Parola OK!")
    else:
        print("Parola NOK!")