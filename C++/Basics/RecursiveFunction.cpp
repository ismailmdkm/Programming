#include <iostream>
using namespace std;
// debug and understand the scope of 'x'
void func(int &n) {
  cout << n << endl;
  n--;
  if (n > 0)
    func(n);
}
int main() {
  int countDown = 5;
  func(countDown);
  return 0;
}