import itertools
def guessables(num):
    guesses = []
    for p in itertools.permutations(range(1,10),num):
        if p[0] != 0:
            guesses.append(''.join(map(str, p)))
    return guesses

def odo_list (listt) :
    odo_list_final = []
    for num in listt :
        if num == "".join(sorted(num)) :
            odo_list_final.append(num)
    return odo_list_final

k=3
listt = guessables(k)
print(odo_list(listt))
