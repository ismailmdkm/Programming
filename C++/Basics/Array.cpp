#include <iostream>
using namespace std;

int main() {
  int numbers[5] = {7, 5, 6, 12, 35}; // many ways to initialize - refer notes
  //  Printing array elements
  for (int i = 0; i < 5; ++i) {
    cout << numbers[i] << "  ";
  }
  // get new 5 numbers
  cout << "\nEnter 5 numbers: " << endl;
  //  store input from user to array
  for (int i = 0; i < 5; i++) {
    cin >> numbers[i];
  }
  cout << "The numbers are: ";
  //  print array elements
  for (int n = 0; n < 5; ++n) {
    cout << numbers[n] << "  ";
  }
  return 0;
}