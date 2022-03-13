#include <iostream>
using namespace std;

int main() {
  int a[5] = {1, 2, 3, 4, 5};
  int *p;
  p = new int[5];
  p[2] = 15;
  p[0] = 5;
  p[1] = 10;
  cout << "Value of p[0] : " << p[0] << endl;
  cout << "Value of p[1] : " << p[1] << endl;
  cout << "Value of p[2] : " << p[2] << endl;
  cout << "Value of p[3] : " << p[3] << endl;
  cout << "Value of p    : " << p << endl;
  cout << "Value in p - '*p' : " << *p << endl;
  cout << "Address of p - '&p' : " << &p << endl;
  cout << "Address of p[0] : " << &p[0] << endl;
  cout << "Address of p[1] : " << &p[1] << endl;
  cout << "Address of p[2] : " << &p[2] << endl;
  cout << "Address of p[3] : " << &p[3] << endl;
  cout << "Value in p - '*p' : " << *p << endl;
  cout << "Value in next loc *(p+1): " << *(p + 1) << endl;
  delete[] p;
  p = nullptr;
  return 0;
}