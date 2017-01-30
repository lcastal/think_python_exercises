# Exercises 10.1
def nested_sum(t):
    result = 0
    for tx in t:
        for elem in tx:
            result += elem
    return result

# result = nested_sum([[2, 4, 6, 8], [3, 4, 5, 2], [1], [5, 8, 9, 4]])
# print(result)


# Exercises 10.2
def cumsum(t):
    tr = [t[0]]
    for i in range(1, len(t)):
        tr.append(tr[i-1]+t[i])
    return tr

# print(cumsum([1, 2, 4, 9, 1, 5]))


# Exercises 10.3
def middle(t):
    return t[1:len(t)-1]

# print(middle([1, 2, 4, 9, 1, 5]))


# Exercises 10.4
def chop(t):
    t.pop(0)
    t.pop(len(t)-1)

# t = [1, 2, 4, 9, 1, 5]
# chop(t)
# print(t)

# Exercises 10.5
def is_sorted(t):
    r = t[:]
    r.sort()
    for i in range(len(t)):
        if r[i] != t[i]:
            return False
    return True

# print(is_sorted([1, 2, 4, 5, 5, 7, 9, 9]))

# Exercises 10.6
def is_anagram(w, z):
    if len(w) != len(z):
        return False
    t = list(w)
    s = list(z)
    for i in range(len(t)):
        if t[i] in s:
            s.remove(t[i])
        else:
            return False
    return True

# print(is_anagram("aaadaaaidmamm", "madamaiamadam"))


# Exercises 10.7
def has_suplicates(t):
    s = t[:]
    s.sort()
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            return True
    return False

# t = ["a", "d", "l", "i", "m", "c", "v", "b"]
# print(has_suplicates(t))
# print(t)