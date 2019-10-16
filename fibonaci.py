def generate_fib_num(curr_num , prev_num) :
    return curr_num + prev_num

def generate_fib_seq(LIMIT) :
    fib_seq = [1, 2]
    k=0
    fib_seq = [ fib_seq[k] + fib_seq[k-1] while k += 1  if fib_seq[k] + fib_seq[k-1] < LIMIT else break]



LIMIT = 4000000
print(sum(generate_fib_seq(LIMIT)))
