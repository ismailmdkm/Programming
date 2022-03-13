#include <iostream>
using namespace std;
// debug and understand the scope of 'x'
int max(int x, int y){return x > y ? x : y;}
int min(int x, int y){return x < y ? x : y;}
int main() { int (*fp)(int, int);  // declaration of function pointer using signature
  int result;
    fp = max;
  result = (*fp)(10, 5);
  cout << "Max is: " << result << endl;
  fp = min;
  result = (*fp)(10, 5);
  cout << "Min is: " << result << endl;
  return 0;
}