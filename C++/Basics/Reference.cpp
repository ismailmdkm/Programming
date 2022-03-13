#include <iostream>
using namespace std;

int main() {
  int x = 10;
  int &y = x; // y and x to share same memory/address
  x++;
  y++;
  cout << x << endl;
  cout << y << endl;
};