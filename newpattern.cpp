#include<bits/stdc++.h>
using namespace std;

bool check_five(int num){
  return num%5==0;
}
bool check_thirty_five(int num){
  return num%35==0;
}
bool check_seven(int num){
  return num%7==0;
}
string check(int num){
  string result=to_string(num);
  if(check_thirty_five(num)){
    result="35";
  }
  else if(check_five(num)){
    result='5';
  }
  else if(check_seven(num)){
    result='7';
  }
  return result;
}

vector<string> sequence(int n,vector<string> v){
  string a;
  for(int i=1;i<n;i++){
  a=check(i);
    if(a=="5"){
      v.push_back("alpha");
    }
    else if(a=="7"){
      v.push_back("beta");
    }
    else if(a=="35"){
      v.push_back("alpha-beta");
    }
    else{
      v.push_back(a);
    }
  }
  return v;
}

int main(){
	int n;
	cin>>n;
  vector<string> v;
  vector<string> final_sequence=sequence(n,v);
  for(auto i=final_sequence.begin();i<final_sequence.end();i++){
    cout<<*i<<endl;
  }
	return 0;
}
