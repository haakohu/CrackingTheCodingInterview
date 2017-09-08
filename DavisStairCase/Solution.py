#!/bin/python3
# pylint: skip-file
# https://www.hackerrank.com/challenges/ctci-recursive-staircase/problem
# Possible steps
steps = [1,2,3]
def DP(n):
  ways = [0 for x in range(n+1)]
  ways[0] = 1
  for i in range(1,n+1):
    count = 0
    for step in steps:
      remaining = i - step
      if remaining >= 0:
        count += ways[remaining]
    ways[i] = count
  return ways[-1]
      
  

s = int(input().strip())
for a0 in range(s):
  n = int(input().strip())
  print(DP(n))



