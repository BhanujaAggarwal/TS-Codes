def alliquot(n) :
    r=2
    aliq=1
    while r*r < n:
        if n%r ==0:
            aliq += r+ n//r
        r+=1
    if n%r ==0:
        aliq+=r
    return aliq

def gen_amicable_pairs(start, limit) :
    for n in range(start,limit):
        align=alliquot(n)
        if align<n:
            if alliquot(align)==n:
                yield(align,n)

import sys
START = 100000
LIMIT = 1000000
for pair in gen_amicable_pairs(START,LIMIT):
    print(pair)
