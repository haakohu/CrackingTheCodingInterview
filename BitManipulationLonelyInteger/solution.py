#!/bin/python3
# pylint: skip-file
# https://www.hackerrank.com/challenges/ctci-lonely-integer/problem
import sys

def lonely_integer(elements):
  n = len(elements)
  seen = [0 for i in range(101)]
  for element in elements:
    seen[element] += 1
  return seen.index(1)

n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]
print(lonely_integer(a))

