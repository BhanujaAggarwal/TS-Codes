def returnWellOrdered(number, x, k):
	listt = []
	if (k == 0):
		# print(number)
		listt.append(number)

	for i in range( (x + 1), 10):
		returnWellOrdered(number * 10 + i,i, k - 1)
	return listt

# def initailise(final_list) :
	# final_list=(returnWellOrdered(0,0,number_of_digits_of_odometer_reading))
	# return final_list[]

# def find_next_reading :

number_of_digits_of_odometer_reading = 3
final_list=(returnWellOrdered(0,0,number_of_digits_of_odometer_reading))
print(final_list[0])
# print(initailise(final_list))

# def find_next_reading

# for i in final_list :
# 	print(i)
