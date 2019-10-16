#include <bits/stdc++.h>
using namespace std;

int get_direction_x(string s) {
  string dir_x_y="";
  string dir=s.erase(s[0]);
  if (dir == 'N'){
    dir_x_y[0] = 0;
    dir_x_y[1] = 1;
  }
  else if (dir == 'S'){
    dir_x_y[0] = 0;
    dir_x_y[1] = -1;

  }
  else if (dir == 'E'){
    dir_x_y[0] = 1;
    dir_x_y[1] = 0;

  }
  else if (dir == 'W'){
    dir_x_y[0] = -1;
    dir_x_y[1] = 0;

  }
  else if (dir == 'NE'){
    dir_x_y[0] = 1;
    dir_x_y[1] = 1;

  }
  else if (dir == 'NW'){
    dir_x_y[0] = -1;
    dir_x_y[1] = 1;

  }
  else if (dir == 'SE'){
    dir_x_y[0] = 1;
    dir_x_y[1] = -1;
  }
  else{
    dir_x_y[0] = -1;
    dir_x_y[1] = -1;
  }
  return dir_x_y;
}

string terminus (vector<int> lattice_point,vector<string> directions){
  int start_x = lattice_point[0];
  int start_y = lattice_point[1];
  for(auto i=directions.begin();i<directions.end();i++){
    int steps = stoi(directions[i][0]);
    start_x += steps*stoi((get_direction_x(directions[i]))[0]);
    start_y += steps*stoi((get_direction_x(directions[i]))[1]);
  }
}

int main()
{
  vector<int> lattice_point;
  lattice_point.push_back(1);
  lattice_point.push_back(1);
  vector<string> directions;
  directions.push_back("1N");
  directions.push_back("3NW");
  cout<<terminus(lattice_point,directions);
	return 0;
}
