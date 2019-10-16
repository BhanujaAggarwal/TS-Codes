#include <bits/stdc++.h>
using namespace std;
int main(){
  int a[10], b[10] ,c[10];
  int x[10], y[10], z[10];
  int k = 0;
  int i = 1, j = 1;
  while(k < 11){
    x[k] = i;
    y[k] = j;
    z[k] = (i * i * i) + (j * j * j);
    k++;
    if(i == j) {
      i++;
    }
    else {
      j++;
    }
  }

  for(i = 0; i < 10; i++){
    a[i] = x[i] * z[i];
    b[i] = y[i] * z[i];
    c[i] = z[i] * z[i];
  }

  for(i = 0; i < 10; i++){
    cout<<a[i]<<" "<<b[i]<<" "<<c[i]<<endl;
  }
	return 0;
}
