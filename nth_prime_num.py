import math
def isPrime(num) :
    if num == 4 :
        return False
    for i in range(2,int(math.sqrt(num))+1) :
        if num % i == 0 :
            return False
    return True

def find_prime(index) :
    primes = [2,3]
    i = 5
    while len(primes) < (index +1) :
        if isPrime(i) :
            primes.append(i)
            i += 2
        else :
            i += 1
    return primes

LIMIT = 10001
print(find_prime(LIMIT-1)[-1])
