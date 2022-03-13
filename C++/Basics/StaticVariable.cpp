#include <iostream>
using namespace std;
// debug and understand the scope of 'x'
void func() {
  static int num1 = 1;
  int num2 = 1;
  cout << "num1: " << num1 << ", num2: " << num2 << endl;
  num1++;
  num2++;
}
int main() {
  func();
  func();
  func();
  return 0;
}