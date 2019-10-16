import itertools
def all_n_digit_nums(num):
    guesses = []
    for p in itertools.permutations(range(1,10),num):
        if p[0] != 0:
            guesses.append(''.join(map(str, p)))
    return guesses
print(all_n_digit_nums(2))
