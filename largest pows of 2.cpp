#include <bits/stdc++.h>
using namespace std;

bool if_powerof2(int num)
{
	return (ceil(log2(num)) == floor(log2(num)));
}

int max_power_of2(vector<int> sequence)
{
	int maximum=2;
	int current_num,current_power;
	for(auto i=sequence.begin();i<sequence.end();i++)
	{
			current_num=*i;
			current_power=ceil(log2(current_num));
			if(if_powerof2(current_num)==true)
			{
				if(current_power>maximum)
				{
					maximum=current_power;
				}
			}
	}
	return maximum;
}

vector<int> generate_sequence(int num,vector<int> sequence)
{
    while(num!=4)
    {
        sequence.push_back(num);
        if(num%2==0){
            num=num/2;
        }
        else{
            num=num*3+1;
        }
    }
    sequence.push_back(4);
    sequence.push_back(2);
    sequence.push_back(1);
    return sequence;
}

int main()
{
	int n;
	cin>>n;
	vector<int > sequence;
	vector<int > sequence_final=generate_sequence(n,sequence);
	cout<<max_power_of2(sequence_final);

	return 0;
}
