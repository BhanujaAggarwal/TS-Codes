#include<bits/stdc++.h>
using namespace std;
int digits(int n)
{
    return log10(n)+1;
}

bool iskaprekar(int n)
{
	if (n == 1)
	return true;
	int sequence = n * n;
	int count_digits = digits(sequence);
	sequence = n*n; 
	for (int r_digits=1; r_digits<count_digits; r_digits++)
	{
		int eq_parts = pow(10, r_digits);
		if (eq_parts == n)
			continue;
		int sum = sequence/eq_parts + sequence % eq_parts;
		if (sum == n)
		return true;
	}
	return false;
}
int main()
{
for (int i=1000; i<10000; i++){
	if (iskaprekar(i))
	{
		cout<<i<<" ";
	}
}
	return 0;
}
