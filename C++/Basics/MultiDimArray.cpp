#include <iostream>
using namespace std;

int main() {
  int a[2][3] = {{1, 1, 1}, {2, 2, 2}};
  int b[2][3] = {1, 1, 1, 3, 3, 3};
  int c[2][3];
  for (int i = 0; i < 2; i++)
  {
      for (int j = 0; j < 3; j++)
      {
        c[i][j] = a[i][j] + b[i][j];
        cout << c[i][j] <<" ";
      }
      cout << endl;
  }
  return 0;
}