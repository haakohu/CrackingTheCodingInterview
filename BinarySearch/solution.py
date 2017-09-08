#!/bin/python3
# pylint: skip-file
# https://www.hackerrank.com/challenges/ctci-ice-cream-parlor/problem

def binary_search(elements, x):
  low = 0
  high = len(elements) -1
  while low <= high:
    mid = (low + high) // 2
    if elements[mid] == x:
      return mid
    if x < elements[mid]:
      high = mid - 1
    else:
      low = mid + 1
  return -1  # Not found

# n^2 solution, can also solve with sorting and using binary search giving nlgn sol. 
# Can use a hash table as well, giving a linear solution.
def solve(flavors, money, n):
  for i in range(0,n-1):
    remaining = money - flavors[i]
    sublis = (flavors[0:i] + flavors[i+1::])
    if remaining in sublis:
      index = flavors.index(remaining)
      if index == i:
        index = sublis.index(remaining) + 1
      return i+1, index+1 

t = int(input().strip())
for a0 in range(t):
  money = int(input().strip())
  n = int(input().strip())
  flavors = list(map(int, input().strip().split(' ')))
  res = solve(flavors, money, n)
  print("{0} {1}".format(res[0], res[1]))
