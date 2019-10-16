import math
from functools import reduce

def lcm(nums) :
    return reduce(lambda a,b : a*b//math.gcd(a,b) ,list(range(1,nums+1)))

print(lcm(10))
