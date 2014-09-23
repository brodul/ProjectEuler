from math import ceil

MAX_SUM = 1000

for c in xrange(1, MAX_SUM/2):
    ab = MAX_SUM - c
    b = c
    while b > int(ceil(ab/2)):
        a = ab - b
        if a ** 2 + b ** 2 == c ** 2:
            print a, b, c
            print a * b * c
        b = b - 1
