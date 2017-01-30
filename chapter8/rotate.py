
def rotate(parola, offset):
    s_minuscole = ord('a')
    s_maiuscole = ord('A')


    cifrata = ""
    for lettera in parola:
        if(lettera.islower()):
            val = (ord(lettera)-s_minuscole + offset) % 26
            cifrata += chr(s_minuscole+val)
        else:
            val = (ord(lettera)-s_maiuscole + offset) % 26
            cifrata += chr(s_maiuscole+val)

    return cifrata

parola = input("parola da cifrare: ")
offset = int(input("offset: "))

cifrata = rotate(parola, offset)

print("cifrata: "+cifrata)