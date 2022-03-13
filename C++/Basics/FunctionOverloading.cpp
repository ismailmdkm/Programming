//Combination of function name and parameter data type to be unique for function overloading
#include <iostream>
using namespace std;

int add(int, int);
int add(int, int, int);
float add(float, float);
int main() {
  int a = 10, b = 5, c = 2, d;
  d = add(a, b);
  cout << "Result of int:" << d << endl;
  d = add(a, b, c);
  cout << "Result of int:" << d << endl;
  float e = 2.5, f = 3.1f, k;
  k = add(e, f);
  cout << "Result of float:" << k << endl;
}
int add(int x, int y) { return x + y; }
int add(int x, int y, int z) { return x + y + z; }
float add(float x, float y) { return x + y; }