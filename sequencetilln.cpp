#include<bits/stdc++.h>
using namespace std;
int main(){
	int n;
	cin>>n;
	int line_number=1;
	int character=1;
	while(character!=n+1){
		line_number=character/2;
		while(line_number-- && character!=n+1)
		{
			cout<<character<<" ";
			character++;
		}
		cout<<endl;
	}
	return 0;
}
