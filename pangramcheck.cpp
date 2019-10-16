#include<bits/stdc++.h>
using namespace std;
bool checkPangram (string str){
    vector<bool> check(26, false);
    int index;
    int len = str.length();
    for (int i = 0; i < len; i++){
        if (str[i] >= 'A' && str[i] <= 'Z'){
          index = str[i] - 'A';
        }
        else if(str[i] >= 'a' && str[i] <= 'z'){
          index = str[i] - 'a';
        }
        check[index] = true;
    }
    for (int i = 0; i <= 25; i++){
        if (!check[i]){
          return false;
        }
      }
    return true;
}

int main(){

    string str = "Pack my box with five dozen liquor jugs.";
    string str2 = "Old brother fox jumps over the lazy dog.";

    if (checkPangram(str)){
      cout <<"Yes";
    }
    else {
      cout <<"No";
    }

    return 0;
}
