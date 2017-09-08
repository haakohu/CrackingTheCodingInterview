#!/bin/python3
# pylint: skip-file
# https://www.hackerrank.com/challenges/ctci-big-o/problem
from math import sqrt

# Can add a list to keep track of primes, but too much memory for hackerrank...
def is_prime(n):
  if n == 2:
    return True
  if n == 1 or n % 2 == 0:
    return False
  for num in range(3, int(sqrt(n)+1),2):
    if n % num == 0:
      return False
  return True
    
    
p = int(input().strip())
for a0 in range(p):
    n = int(input().strip())
    if is_prime(n):
      print("Prime")
    else:
      print("Not prime")
