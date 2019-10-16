import random
import itertools

def prob(x):
    count = x-1 if x <= 7 else 13-x
    return 1000*count/36

expected = [0] + [prob(x) for x in range(1, 13)]
results = [0] * 13

def die_roll():
    return random.randint(1, 6)

for count in itertools.count(start=1):
    results[die_roll() + die_roll()] += 1

    if all(1000* r/count == e
           for r, e in itertools.izip(results, expected)):
        break

print count
