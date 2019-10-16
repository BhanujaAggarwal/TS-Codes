import operator
import functools
def make_list(num,digits) :
    digit_list = []
    for i in range(0,digits) :
        digit_list.append(i)
    return digit_list

def multiply_all(input_list) :
    return functools.reduce(operator.mul,input_list,1)


num="7316717653133062491922511967442657474235534"
digits= len(num)
i =0
make_num = int(num[i:i+13])
make_list = list(make_num)
curr_product = multiply_all(make_list)
