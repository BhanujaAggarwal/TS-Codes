#include <bits/stdc++.h>
using namespace std;
#define SIZE 26

map<char,int> printCharWithFreq(string str)
{
  map<char,int> m;
  int n = str.size();
  int freq[SIZE];
  memset(freq, 0, sizeof(freq));
  for (int i = 0; i < n; i++)
      freq[str[i] - 'a']++;
  for (int i = 0; i < n; i++) {
      if (freq[str[i] - 'a'] != 0) {
        m[str[i]] = freq[str[i] - 'a'];
          freq[str[i] - 'a'] = 0;
        }
      }
  return m;
}

int count_of_vowels_and_consonants(map<char,int> m){
  int impurity_index = 0;
  for(auto i=m.begin() ;i<m.end();i++){
    if (m[i] > 3){
      impurity_index += 3;
    }
    else if (m[i] > 2){
      impurity_index += 1;
    }
    else if (m[i] == 2){
      if (i == 'a' || i == 'e' || i == 'i' || i == 'o' || i == 'u'){
				impurity_index += 0.5;
      }
      else {
      impurity_index += 0.7;
    }
    }
  }
  return impurity_index;
}


int main() {
  string input = "Pack my box with five dozen liquor jugs";
  cout<<find_inpurity_index(generate_freq(input));
  return  0;
}
