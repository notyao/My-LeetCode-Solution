def reverseString(s):
    r = list(s)
    i = 0
    j = len(r) - 1
    while i < j:
        r[i], r[j] = r[j], r[i]
        i += 1
        j -= 1
    return "".join(r)

def reverseString(s):
    l = len(s)
    if l < 2:
        return s
    return reverseString(s[l/2:]) + reverseString(s[:l/2])

def reverseString(s):
    return s[::-1]

