from itertools import groupby

def get_runs_of_same_num(s) :
    return [list(group[1]) for group in groupby(s)]

def rle_one_run(run) :
    size =len(run)
    if size <= 2 :
        return size * run[0]
    return str(size) + run[0]

def rle(s) :
    return "".join([rle_one_run(block) for block in get_runs_of_same_num(s)])

print(rle("aaaabbbaaaaa"))
