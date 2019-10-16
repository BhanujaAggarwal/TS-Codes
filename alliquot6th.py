def aliquotSum(num) :
	aliquot = 0
	for i in range(1,num) :
		if (num % i == 0) :
			 aliquot= aliquot + i

	return aliquot
num = int(input())
print(aliquotSum(num))
