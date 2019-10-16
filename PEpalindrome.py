def palindrome(num) :
    return str(num) == (str(num))[::-1]
    # return str(num) == "".join(reversed(str(num)))
def largest_3digit_palindrome (n) :
    palindrome_list = []
    rangee= list(range(int('9'*n),int('9'* (n-1)),-1))
    return max([n1*n2 for n1 in rangee for n2 in rangee if palindrome(n1*n2)])
n=3
print(largest_3digit_palindrome(n))
