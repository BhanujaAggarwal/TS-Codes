import string

all_alphabets = set(string.ascii_lowercase)

def isPangram(input_string):
	return set(input_string.lower()) >= all_alphabets

input1 = "Pack my box with five dozen liquor jugs"
input2 = "Old brother fox jumps over the lazy dog"
if(isPangram(input1) == True):
	print("Yes")
else:
	print("No")
if(isPangram(input2) == True):
	print("Yes")
else:
	print("No")
