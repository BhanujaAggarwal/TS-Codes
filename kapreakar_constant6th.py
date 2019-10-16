def digits_of_given_number(n):
    digits = [0] * 4;
    for i in range(4):
        digits[i] = n % 10
        n = int(n // 10)
    return digits

def maximum_no_formed_by_digits(digits):
    digits.sort()
    maximum=0
    for i in range(3, -1, -1):
        maximum = maximum * 10 + digits[i]
    return maximum

def minimum_no_formed_by_digits(digits):
    digits.sort()
    minimum=0
    for i in range(4):
        minimum = minimum * 10 + digits[i]
    return minimum

def iskaprekarconstant(n,previous):
    if (n == 0):
        return 0
    previous=n
    digits = digits_of_given_number(n)
    difference = abs(maximum_no_formed_by_digits(digits) - minimum_no_formed_by_digits(digits))

    if(difference == previous):
        return difference

    return iskaprekarconstant(difference,previous)

def kaprekar(n):
    rev=0
    print(iskaprekarconstant(n,rev))

print(kaprekar(9812))
