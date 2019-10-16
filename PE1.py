def multiple_of_3_or_5(num) :
    return (num % 3 ==0 or num % 5==0)

def generate_multiples_3_or_5(n) :
    multiples_list= []
    for i in range(3,n) :
        if multiple_of_3_or_5(i) :
            multiples_list.append(i)
    return multiples_list

LIMIT= 1000
print(sum(generate_multiples_3_or_5(LIMIT)))
