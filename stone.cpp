#include <bits/stdc++.h>
using namespace std;

int main()
{
  string input="RP, RR, SP, SR";
  int n=input.length();
  int win=0,loose=0,draw=0;
  for(int i=0;i<n;i++){
    if(input[i]!=',' && input[i]!=' '){
      char input_1 = input[i];
      char input_2 = input[i+1];
      if(input_1 == input_2){
        draw++;
      }
      else{
        if(input_1=='R'){
          if(input_2=='P'){
            loose++;
          }
          else{
            win++;
          }
        }

        else if(input_1=='P'){
          if(input_2=='S'){
            loose++;
          }
          else{
            win++;
          }
        }

        else{
          if(input_2=='R'){
            loose++;
          }
          else{
            win++;
          }
        }

      }
      i++;
    }

  }
  cout<<"+"<<win<<", "<<"-"<<loose<<", "<<"="<<draw;


	return 0;
}
