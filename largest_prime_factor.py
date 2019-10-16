import math
def factors(num) :
    factors_list = []
    for i in range(2,int(math.sqrt(num))) :
        while num % i == 0 :
            factors_list.append(i)
            num /= i
    return factors_list

n = 600851475143
print(factors(n)[-1])
