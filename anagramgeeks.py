NO_OF_CHARS = 58
def areAnagram(str1, str2) :

	count1 = [0] * NO_OF_CHARS
	count2 = [0] * NO_OF_CHARS

	for i in str1:
		count1[ord(i)]+= 1

	for i in str2:
		count2[ord(i)]+= 1

	if len(str1) != len(str2):
		return 0

	for i in range(NO_OF_CHARS):
		if count1[i] != count2[i]:
			return 0

	return 1

file1 = open("sowpods.txt","r")
contents =file1.readlines()
for x in contents :
	word1 = x
	for y in contents :
		word2 =y
		if (x != y and areAnagram(word1,word2)==1) :
			result= word1 + " " + word2
			print(result)
