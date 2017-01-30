# exercise 10.8
import random


def has_suplicates(t):
    s = t[:]
    s.sort()
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            return True
    return False


def generate_date():
    year = random.randint(1950, 2017)
    month = random.randint(1, 12)
    if month == 2:
        if year % 4 == 0:
            day = random.randint(1, 29)
        else:
            day = random.randint(1, 28)
    elif (month < 8 and month % 2 != 0) or (month >= 8 and month % 2 == 0):
        day = random.randint(1, 31)
    else:
        day = random.randint(1, 30)

    return str(day)+"-"+str(month)


t = []
count_match = 0
for j in range(1000):
    for i in range(23):
        t.append(generate_date())
    if has_suplicates(t):
        count_match += 1

prob = count_match/1000.00
print("Over 1000 experiments, the probability got is: %f" %prob)