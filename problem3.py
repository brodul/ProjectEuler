#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143 ?


number = long(600851475143)
prime = 2
while prime ** 2 < number:
    while not number % prime:
        number = number / prime
    prime = prime + 1

print number
