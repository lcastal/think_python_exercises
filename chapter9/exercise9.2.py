

def has_no_e(word):
    if ("e" in word) or ("E" in word):
        return True
    else:
        return False


def withoute():
    count, total_line = 0, 0
    fin = open("words.txt")

    for line in fin:
        line = line.strip()
        if has_no_e(line):
            count += 1
        total_line += 1

    return count/total_line * 100


print("%d" % withoute())