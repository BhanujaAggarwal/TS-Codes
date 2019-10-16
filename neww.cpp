#include<bits/stdc++.h>
using namespace std;

int count_divisors(int num) {
	int count_of_divisors;=0;
	for(int i=2;i <= sqrt(n);i++){
		if (n % i == 0){
			count_of_divisors ++;
			if (n / i != i)
				count_of_divisors ++;
		}
		return count_of_divisors;
}

bool is_num_of_divisors_even(int divisors_count) {
	return count_divisors(divisors_count)%2==0
}

int main(){
	int num=100;
	if(is_num_of_divisors_even(count_divisors(num)))
	cout<<"CLOSED"<<" ";
	else
	cout<<"OPEN"<<" ";
	return 0;
}
