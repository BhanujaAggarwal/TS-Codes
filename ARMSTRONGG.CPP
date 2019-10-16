#include <bits/stdc++.h>
using namespace std;
vector<int> findArmstrong(int low, int high)
{
  vector<int> sequence;
	for (int i = low+1; i < high; ++i) {
		int x = i;
		int n = 0;
		while (x != 0) {
			x /= 10;
			++n;
		}
		int pow_sum = 0;
		x = i;
		while (x != 0) {
			int digit = x % 10;
			pow_sum += pow(digit, n);
			x /= 10;
		}
		if (pow_sum == i) {
      sequence.push_back(i);
    }
	}
  return sequence;
}
int main()
{
  int num1,num2;
  cin>>num1>>num2;
  vector<int> sequence=findArmstrong(num1, num2);
  for(auto i=sequence.begin();i<sequence.end();i++)
  {
      cout<<*i<<" ";
  }
	return 0;
}
