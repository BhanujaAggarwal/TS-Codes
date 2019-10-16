#include <bits/stdc++.h>
using namespace std;

bool check_ambiguous_date(int date ,int month){

  return date < 12 ;
}

int main()
{

  string input="05/05/1999";
  string date_in_string = input.substr(0,2);
  string month_in_string = input.substr(3,2);
  int date = stoi(date_in_string);
  int month = stoi(month_in_string);
  if(check_ambiguous_date(date,month)){
    cout<<"Yes , date is ambiguous";
  }
  else{
    cout<<"no , date is not ambiguous";
  }
  
	return 0;
}
