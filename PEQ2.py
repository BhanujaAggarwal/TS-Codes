def generate_next_fib_num(curr_num , prev_num) :
    return curr_num + prev_num

def pick_even_fib_num(fib_num) :
    return fib_num % 2 == 0

def generate_fib_seq(k) :
    fib_seq = []
    fib_seq[0] = 1
    fib_seq[1] = 2
    count = 1
    print(fib_seq[0])
    while(True) :
        next_fib_num = generate_next_fib_num(fib_seq[count] ,fib_seq[count-1])
        if next_fib_num >= k :
            break
        else :
            fib_seq.append(next_fib_num)
            count += 1
    return fib_seq

LIMIT=90
(generate_fib_seq(LIMIT))
