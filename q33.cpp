#include <bits/stdc++.h>
using namespace std;
int main(){
	srand(time(0));

	int freq_of_diff_nums[35] = {0};

	int first_person ,second_person ,sum_on_die ;

	for(int i=0;i<10000;i++){

		first_person = (rand() % 6 + 1);
		second_person = (rand() % 6 + 1);
		sum_on_die = first_person + second_person;
		freq_of_diff_nums[sum_on_die - 1]++;
	}

	for(int j=0;j<36;j++){
		cout<<freq_of_diff_nums[j]<<endl;
	}
	
	return 0;
}
