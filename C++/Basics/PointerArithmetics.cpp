#include <iostream>
using namespace std;

int main() { int arr[5]{2, 4, 6, 8, 10};
  int *ptr = arr;
  cout << "Value in ptr - *ptr:" << *ptr << endl;
  ptr++;
  cout << "After ptr++ - *ptr:" << *ptr << endl;
  ptr--;
  cout << "After ptr-- - *ptr:" << *ptr << endl;
  cout << "*(ptr + 2):" << *(ptr + 2) << endl;
  cout << "Value still same - *ptr:" << *ptr << endl;
  // dealing with another pointer
  int *q = &arr[4];
  cout << "Value of q-p:" << q - ptr << endl;
  cout << "Value of p-q:" <<  ptr - q << endl;
  return 0;
}