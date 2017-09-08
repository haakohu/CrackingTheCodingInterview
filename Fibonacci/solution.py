#!/bin/python3
# pylint: skip-file
# https://www.hackerrank.com/challenges/ctci-queue-using-two-stacks/problem

def fibonacci(n):
  items = [0, 1]
  for i in range(n-1):
    r = items[-1] + items[-2]
    items.append(r)
  return items[-1]
    
n = int(input())
print(fibonacci(n))

