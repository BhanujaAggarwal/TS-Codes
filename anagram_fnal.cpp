#include <bits/stdc++.h>
using namespace std;

string sortWord(string &str)
{
   sort(str.begin(), str.end());
   return str ;
}

bool anagram(string word1,string word2){
  string word1_final=sortWord(word1);
  string word2_final=sortWord(word2);
  return (word1_final==word2_final);
}

int main()
{
  string word1="abcd";
  string word2="dcba";
  if(anagram(word1,word2)){
    cout<<"Yes";
  }
  else{
    cout<<"No";
  }
	return 0;
}
