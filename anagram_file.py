TYPE_OF_CHARS = 26
def Is_Anagram(word1, word2) :

	count1 = [0] * TYPE_OF_CHARS
	count2 = [0] * TYPE_OF_CHARS
	for i in word1:
		if i != " " :
			count1[(ord(i)) - 65] += 1

	for i in word2:
		if i != " " :
			count2[(ord(i)) - 65] += 1

	for i in range(TYPE_OF_CHARS) :
		if count1[i] != count2[i] :
			return 0
	return 1

file1 = open("sowpods.txt","r")
contents =file1.readlines()
for x in contents :
	word1 = x.strip()
	for y in contents :
		word2 =y.strip()
		if (x != y and Is_Anagram(word1,word2)==1) :
			result= word1 + " " + word2
			print(result)
