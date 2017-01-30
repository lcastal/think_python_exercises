
def avoid(word, chars):
    for char in chars:
        if char in word:
            return False
    return True


def numberwordwithout(chars):

    fin = open("words.txt")
    count = 0
    for line in fin:
        line = line.strip()

        if avoid(line, chars):
            count += 1

    return count

"""
start = ord("a")
end = ord("z")
while start <= end:
    print("parole senza la "+chr(start)+" : %d" %numberwordwithout(chr(start)))
    start += 1
"""
"""
"""

word = "aaaaa"
count = numberwordwithout(word)
result = word

for i in range(0,len(word)):
    for j in range(0,26):
        temp_result = word[0:i]+chr(ord(word[i:i+1])+j)+word[i+1:]
        temp_count = numberwordwithout(temp_result)
        if temp_count < count:
            count = temp_count
            result = temp_result

print("i caratteri proibiti che escludono il minor numero di parole sono: "+result)
print("le parole escluse sono: "+str(count))

while True:
    chars = input("caratteri proibiti: ")
    if chars == "done":
        break
    result = numberwordwithout(chars)
    print(result)