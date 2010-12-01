import string
max = 998001
a = 999


def lol(c):
    l = []
    for b in range(600, c):
        for a in range(600, c):
            if check(a, b):
                    l.append(a * b)
    return l


def check(a, b):
    num = list(str(a * b))
    inum = num[:]
    inum.reverse()
    if num[:3] == inum[:3]:
        return num

print lol(a)
