
def compute_pow(num):
    return pow(2,num)
def sum_of_digits(num):
    total=0
    for digit in str(num):
        total=total+int(i)
    return total

req_power=10000
print(sum_of_digits(compute_pow(req_power)))
