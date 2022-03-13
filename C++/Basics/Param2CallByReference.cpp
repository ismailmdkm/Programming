// Combination of function name and parameter data type to be unique for
// function overloading
#include <iostream>
using namespace std;

void swap(int &a, int &b) {
  int temp;
  temp = a;
  a = b;
  b = temp;
}
int main() {
  int x = 10, y = 20, z;
  cout << "Before swapping: x=" << x << ", y=" << y << endl;
  swap(x, y);
  cout << "After swapping: x=" << x << ", y=" << y << "!!!Swapped as expected!!!"
       << endl;
  return 0;
}