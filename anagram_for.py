TYPE_OF_CHARS = 26
def Anagram(word1, word2) :

	count1 = [0] * TYPE_OF_CHARS
	count2 = [0] * TYPE_OF_CHARS
	for i in word1:
		if i != " " :
			count1[ord(i) - 97] += 1

	for i in word2:
		if i != " " :
			count2[ord(i) - 97] += 1

	for i in range(TYPE_OF_CHARS) :
		if count1[i] != count2[i] :
			return 0
	return 1

word1 = "dcd c"
word2 = "dccd"
if Anagram(word1.lower(), word2.lower()) :
	print("Yes")
else:
	print("No")
