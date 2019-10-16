#include<bits/stdc++.h>
using namespace std;

int digits(int n)
{
    return log10(n)+1;
}

vector<int> armstrong_list(int high,int low)
{
  vector<int> sequence;
  for(int i=low+1;i<high;i++)
  {
    int x=i;
    int sum=0;
    int digits_in_x=digits(x);
    while(x!=0)
    {
      int current_digit=x%10;
      sum=sum+pow(current_digit,digits_in_x);
      x=x/10;
    }
    if(sum==x)
    {
      sequence.push_back(x);
    }
  }
  return sequence;
}
int main()
{
  int high,low;
  cin>>high>>low;
  vector<int> sequence=armstrong_list(high,low);
  for(auto k=sequence.begin();k<sequence.end();k++)
  {
    cout<<*k<<endl;
  }

}
