"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
# Memory usage of set_ is 6MB
set_ = set(xrange(2, 2*10**6))

for i in xrange(2, 2*10**6):
    if i in set_:
        for n in xrange(i**2, 2*10**6, i):
            set_.discard(n)

print set_
print sum(set_)
