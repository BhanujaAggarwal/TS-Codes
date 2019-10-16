import string

def generate_freq (input) :
	all_freq = {}
	for i in input:
		if i in all_freq:
			all_freq[i] += 1
		else:
			all_freq[i] = 1
	return all_freq

def find_inpurity_index(all_freq) :
	impurity_index = 0
	for i in all_freq :
		if all_freq[i] > 3 :
			impurity_index += 3
		elif all_freq[i] > 2 :
			impurity_index += 1
		elif all_freq[i] == 2 :
			if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u') :
				impurity_index += 0.5
			else :
				impurity_index += 0.7
	return impurity_index


input_string = "Pack my box with five dozen liquor jugs"
input = input_string.lower().replace(" ", "")
print(find_inpurity_index(generate_freq(input)))
