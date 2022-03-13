//Combination of function name and parameter data type to be unique for function overloading
#include <iostream>
using namespace std;

template <class T, class R>

T add(T x, R y) { return x + y; }
int main() {
  int a = 10, b = 5, d;
  d = add(a, b);
  cout << "Result of int:" << d << endl;
  float e = 2.5f, f = 3.1f, k;
  k = add(e, f);
  cout << "Result of float:" << k << endl;
  k = add(a, f); // Note: First operand data type is in the result. We can do add((float)a, f); to get floating point result.
  cout << "Result of int/float:" << k << endl;
  k = add(e, b);
  cout << "Result of float/int:" << k << endl;
}