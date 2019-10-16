def generate_n_num(n) :
    return list(range((10**(n-1)),(10**n)))

def generate_odometer(all_n_num) :
    odo_list =[]
    for number in all_n_num:
        num_string = str(number)
        print(sorted(num_string))

        if (num_string == sorted(num_string)) :
            odo_list.append(number)
    return odo_list




n=2
all_n_num = generate_n_num(n)
print(generate_odometer(all_n_num))
