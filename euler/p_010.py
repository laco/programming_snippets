# Summation of primes
#
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.


def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    k = 3
    while k*k <= n:
        if n % k == 0:
            return False
        k += 2
    return True


def primes(smaller_than):
    for i in range(2, 2*1000*1000):
        if is_prime(i):
            yield i

print(sum(primes(2*1000*1000)))
