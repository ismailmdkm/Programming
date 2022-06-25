#include <iostream>
#include<iterator> // for iterators
#include<vector> // for vectors
using namespace std;
int main() {
  vector<int> v1 = {1, 2, 3, 4, 5};
  // Declaring iterator to a vector
  vector<int>::iterator v1Ptr1;
  vector<int>::iterator v1Ptr2;
  // Displaying vector elements using begin() and end()
  for (v1Ptr1 = v1.begin(); v1Ptr1 < v1.end(); v1Ptr1++)
    cout << *v1Ptr1 << " ";
  cout << endl;
  // Another way without iterators
  for (int i = 0; i < size(v1); i++)
    cout << v1[i] << " ";
  cout << endl;
  // Better way from C+11
  for (auto num : v1)
    cout << num << " ";
  cout << endl;
  v1Ptr2 = v1.begin();
  cout << "Iterator position before advancing: " << *v1Ptr2 << "\n";
  // Using advance() to increment iterator position points to 4
  advance(v1Ptr2, 3);
  // Displaying iterator position
  cout << "Iterator position after advancing: " << *v1Ptr2 << "\n";

  v1Ptr1 = v1.begin();
  v1Ptr2 = v1.end();
  // Using next() & prev()
  auto v1Ptr1A = next(v1Ptr1, 3);
  auto v1Ptr2A = prev(v1Ptr2, 3);
  cout << "The position of new iterator using next() is : " << *v1Ptr1A << endl;
  cout << "The position of new iterator using prev() is : " << *v1Ptr2A << endl;

  vector<int> ar1 = {10, 20, 30};
  vector<int>::iterator ptr = v1.begin();
  advance(ptr, 3);
  copy(ar1.begin(), ar1.end(), inserter(v1, ptr));
  cout << "The new vector after inserting elements is : ";
  for (int &x : v1)
    cout << x << " ";
  return 0;
}