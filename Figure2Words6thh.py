one = [ "", "one ", "two ", "three ", "four ",
		"five ", "six ", "seven ", "eight ",
		"nine ", "ten ", "eleven ", "twelve ",
		"thirteen ", "fourteen ", "fifteen ",
		"sixteen ", "seventeen ", "eighteen ",
		"nineteen "];
ten = [ "", "", "twenty ", "thirty ", "forty ",
		"fifty ", "sixty ", "seventy ", "eighty ",
		"ninety "];

def numberToWords(n, s):

	str = "";

	if (n > 19):
		str += ten[n // 10] + one[n % 10];
	else:
		str += one[n];

	if (n):
		str += s;

	return str;
def figureToWords(n):
	word = "";

	word = word + numberToWords((n // 10000000),
							"crore ");

	word = word + numberToWords(((n // 100000) % 100),
								"lakh ");

	word = word + numberToWords(((n // 1000) % 100),
							"thousand ");

	word = word + numberToWords(((n // 100) % 10),
							"hundred "); 

	if (n > 100 and n % 100):
		word = word + "and ";

	word = word + numberToWords((n % 100), "");

	return word;

n = 1997;
print(figureToWords(n));
