#!/bin/python3
# pylint: skip-file
# https://www.hackerrank.com/challenges/ctci-making-anagrams/problem
def number_needed(word1, word2):
  count = [0 for i in range(26)]
  for char in word1: 
    count[ord(char) - ord('a')] += 1
  for char in word2:
    count[ord(char) - ord('a')] -= 1
  return sum(map(lambda x: abs(x), count))

a = input().strip()
b = input().strip()

print(number_needed(a, b))

