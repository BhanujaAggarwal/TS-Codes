#include <bits/stdc++.h>
using namespace std;
string one_digit_word[] = { "", "one ", "two ", "three ", "four ",
  "five ", "six ", "seven ", "eight ",
  "nine ", "ten ", "eleven ", "twelve ",
  "thirteen ", "fourteen ", "fifteen ",
  "sixteen ", "seventeen ", "eighteen ",
  "nineteen "
};

string ten_digit_word[] = { "", "", "twenty ", "thirty ", "forty ",
  "fifty ", "sixty ", "seventy ", "eighty ",
  "ninety "
};

string numToWords (int num, string s){
  string word = "";
  if (num > 19)
    word = word + ten_digit_word[num / 10] + one_digit_word[num % 10];
  else
    word = word + one_digit_word[num];
  if (num)
    word = word + s;

  return word;
}

string convertToWords (long num){
  string words;
  words = words + numToWords ((num / 10000000), "crore ");
  words = words + numToWords (((num / 100000) % 100), "lakh ");
  words = words + numToWords (((num / 1000) % 100), "thousand ");
  words = words + numToWords (((num / 100) % 10), "hundred ");
  if (num > 100 && num % 100)
    words += "and ";
  words = words + numToWords ((num % 100), "");
  return words;
}

int main (){
  long long int num;
  cin >> num;
  cout << convertToWords (num) << endl;

  return 0;
}
