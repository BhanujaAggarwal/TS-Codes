def isPrime(num) :
    if num == 2 :
        return True
    for i in range(2,(num/2)+1) :
        if num % i == 0 :
            return False
    return True

def max_prime_factor(num) :
    end = (num/2) + 1
    while (True) :
        if (num % end == 0 and isPrime(end)) :
            return end
        else :
            end -= 1

num = 13195
print(max_prime_factor(num))
