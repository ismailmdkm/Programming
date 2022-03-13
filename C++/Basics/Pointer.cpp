#include <iostream>
using namespace std;

int main() {
  int var;
  int *ptr;
  ptr = &var;
  var = 10;
  cout << "Value of Var - 'var'     : " << var << endl;
  cout << "Address of var - '&Var'  : " << &var << endl;
  cout << "Value of ptr - 'ptr'     : " << ptr << endl;
  cout << "Value in ptr - '*ptr'    : " << *ptr << endl;
  cout << "Address of ptr - '&ptr'  : " << &ptr << endl;
  var = 20;
  cout << "Value of Var - 'var'     : " << var << endl;
  cout << "Address of var - '&Var'  : " << &var << endl;
  cout << "Value of ptr - 'ptr'     : " << ptr << endl;
  cout << "Value in ptr - '*ptr'    : " << *ptr << endl;
  cout << "Address of ptr - '&ptr'  : " << &ptr << endl;
  // note: same memory is retained
}