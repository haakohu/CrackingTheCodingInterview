#!/bin/python3
# pylint: skip-file
# https://www.hackerrank.com/challenges/ctci-ransom-note/problem

def ransom_note(magazine, ransom):
  dic = {}
  for word in magazine:
    if word in dic.keys():
      dic[word] += 1
    else:
      dic[word] = 1
  for word in ransom:
    if not word in dic.keys() or dic[word] == 0:
      return False
    dic[word] -= 1
  return True

m, n = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')
ransom = input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print("Yes")
else:
    print("No")
    

