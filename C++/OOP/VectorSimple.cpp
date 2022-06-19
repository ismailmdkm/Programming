#include <iostream>
#include <vector>
using namespace std;

int main() {
  // initialize a vector of int type
  vector<int> numbers = {1, 100, 10, 70, 100};
  numbers.push_back(55);
  // print the vector
  cout << "Numbers are: ";
  for (auto &num : numbers) {
    cout << num << ", ";
  }
  return 0;
}