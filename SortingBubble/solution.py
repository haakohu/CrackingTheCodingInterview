#!/bin/python3
# pylint: skip-file
# https://www.hackerrank.com/challenges/ctci-bubble-sort/problem

'''
for (int i = 0; i < n; i++) {
    // Track number of elements swapped during a single array traversal
    int numberOfSwaps = 0;
    
    for (int j = 0; j < n - 1; j++) {
        // Swap adjacent elements if they are in decreasing order
        if (a[j] > a[j + 1]) {
            swap(a[j], a[j + 1]);
            numberOfSwaps++;
        }
    }
    
    // If no elements were swapped during a traversal, array is sorted
    if (numberOfSwaps == 0) {
        break;
    }
}
'''
def swap(i1, i2, array):
  item1 = array[i1]
  item2 = array[i2]
  array[i2] = item1
  array[i1] = item2


def solve(a, n):
  count = 0
  for i in range(n):
    numberOfSwaps = 0
    for j in range(n-1):
      if a[j] > a[j+1]:
        swap(j, j+1, a)
        numberOfSwaps += 1
    count += numberOfSwaps
    if numberOfSwaps == 0:
      break
  print("Array is sorted in {0} swaps.".format(count))
  print("First Element:",  a[0])
  print("Last Element:", a[-1])


n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
solve(a,n)
