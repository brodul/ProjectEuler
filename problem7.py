def prime_finder_gen(prime_num_set):

    def is_prime(num):
        for prime in prime_list:
            if num % prime == 0:
                return False
        return True

    num = 5
    prime_num = 0
    prime_list = [2, 3]
    for prime in prime_list:
        yield prime
        prime_num += 1
    while not prime_num == prime_num_set:
        if is_prime(num):
            prime_list.append(num)
            yield num
            prime_num += 1
        num += 2

for prime in prime_finder_gen(10001):
    result = prime
print result
