#include <bits/stdc++.h>
using namespace std;
int sumOfDiv(int x)
{
	int sum =  1;
	for(int i = 2;i <= sqrt(x);i++){
		if (x % i == 0){
			sum += i;
			if (x / i != i)
			sum += x / i;
		}
	}
	return sum;
}
bool isAmicable(int a, int b){
	return (sumOfDiv(a) == b &&
	sumOfDiv(b) == a);
}
vector< pair <int,int> > generate_sequence(int arr[],vector< pair <int,int> > sequence,int n){
	for (int i = 0; i < n; i++){
		for (int j = i + 1; j < n; j++){
			if (isAmicable(arr[i], arr[j])){
				sequence.push_back( make_pair(arr[i],arr[j]) );
			}
		}
	}
	return sequence;
}

int main()
{
	int n1=900000;
	int num_list[n1];
	int k=100000;
	for(int i=0;i<n1;i++){
		num_list[i]=k;
		k++;
	}
	vector< pair <int,int> > sequence;
	vector< pair <int,int> > sequence_final=generate_sequence(num_list,sequence,n1);
	for(auto i=sequence_final.begin();i<sequence_final.end();i++){
		cout << sequence_final.first << " "<< sequence_final.second << endl;
	}
	return 0;
}
