def generate_ranks(new_dict,count2) :
	ranks =[]
	rank = 0
	for i in range(0, count2) :
		rank += 1
		if (new_dict[roll_num[i]] == new_dict[roll_num[i +1]] and i+1 < count2 ) :
			ranks.append(rank)
			ranks.append(rank)
			ranks += 1
		else :
			ranks.append(rank)


roll_num = []
marks = []
count=0;
new_dict = {}
ranklist=open("ranklist.txt","r")
for word in ranklist.read().split() :
	if (count % 2 == 0) :
		roll_num.append(word)
	else :
		marks.append(word)
	count += 1
count = count / 2
count2 = count
while count :
	count -= 1
	new_dict[roll_num[count]] = marks[count]
final_dict = sorted(new_dict.items(), key = lambda kv:(kv[1], kv[0]))
generate_ranks(new_dict , count2)

print(final_dict)
