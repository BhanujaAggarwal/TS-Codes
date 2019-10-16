// C++ program to demonstrate working of
// Kaprekar constant
#include<bits/stdc++.h>
using namespace std;

// This function checks validity of kaprekar's
// constant. It returns kaprekar's constant for
// any four digit number "n" such that all digits
// of n are not same.
int kaprekarRec(int n, int &prev)
{
	if (n == 0)
	return 0;

	// Store current n as previous number
	prev = n;

	// Get four digits of given number
	int digits[4];
	for (int i=0; i<4; i++)
	{
	digits[i] = n%10;
	n = n/10;
	}

	// Sort all four dgits in ascending order
	// And giet in the form of number "asc"
	sort(digits, digits+4);
	int asc = 0;
	for (int i=0; i<4; i++)
	asc = asc*10 + digits[i];

	// Get all four dgits in descending order
	// in the form of number "desc"
	sort(digits, digits+4, std::greater<int> ());
	int desc = 0;
	for (int i=0; i<4; i++)
	desc = desc*10 + digits[i];

	// Get the difference of two numbers
	int diff = abs(asc - desc);

	// If difference is same as previous, we have
	// reached kaprekar's constant
	if (diff == prev)
		return diff;

	// Else recur
	return kaprekarRec(diff, prev);
}

// A wrapper over kaprekarRec()
int kaprekar(int n)
{
	int prev = 0;
	return kaprekarRec(n, prev);
}

// Driver code
int main()
{
	// Trying few four digit numbers, we
	// always get 6174
	cout << kaprekar(1000) << endl;
	cout << kaprekar(1112) << endl;
	cout << kaprekar(9812) << endl;
	return 0;
}
