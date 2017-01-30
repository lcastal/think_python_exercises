def morethan20():
    count = 0
    fin = open("./words.txt")

    for line in fin:
        line = line.strip()
        if " " in line:
            line.replace(" ","")

        if len(line) >= 20:
            print(line)

morethan20()