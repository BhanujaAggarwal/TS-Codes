#include<bits/stdc++.h>
using namespace std;

int reverse(int n)
{
  int t=0;
  while(n!=0)
  {
    t=(t*10)+(n%10);
    n=n/10;
  }
  return t;
}

bool is_palidrome(int n)
{
  return reverse(n)==n;
}

int digits(int n)
{
    return log10(n)+1;
}

bool all_nine(int n)
{
    return digits(n+1)>digits(n);
}
string reversed_palindrome(int n)
{
  string final1;
  string final2;
  int mid=(digits(n)+1)/2;
  if(digits(n)%2==0)
  {
    int half_number=n/(pow(10,mid));
    final1=to_string(half_number)+to_string(reverse(half_number));

    int half_number1=half_number+1;
    final2=to_string(half_number1)+to_string(reverse(half_number1));
    if(stoi(final1)>n)
    return final1;
    return final2;
  }
  else
  {
    int half_number=n/(pow(10,mid));
    int mid_digit=(n/(pow(10,mid-1)));
    mid_digit=mid_digit%10;
    if(mid_digit==9)
    {
        final1=to_string(half_number+1)+'0'+to_string(reverse(half_number+1));
        return final1;
    }else{
    final1=to_string(half_number)+to_string(mid_digit)+to_string(reverse(half_number));
    final2=to_string(half_number)+to_string(mid_digit+1)+to_string(reverse(half_number));
    }
    if(stoi(final1)>n)
    return final1;
    return final2;
  }
}
string nextpalindrome(int n)
{
  string number;
  number=to_string(n);
  if(all_nine(n))
  {
    n=n+2;
    number=to_string(n);
    return number;
  }
  return reversed_palindrome(n);
}

int main()
{
    int n;
    cin>>n;
    cout<<nextpalindrome(n);

    return 0;
}
