import math
def findArmstrong(low,high):
    sequence=[]
    for i in range(low+1,high):
        digits=int(math.log10(i)+1)
        pow_sum=0
        x=i;
        print(x)
        while (x != 0):
		    digitt = x % 10
			pow_sum = pow_sum + math.pow(digitt, digits)
			x = x / 10
        print(pow_sum)
        if(pow_sum==i):
            sequence.append(i)
    return sequence

num1=100
num2=400
print(findArmstrong(num1,num2))
