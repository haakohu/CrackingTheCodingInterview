# pylint: skip-file
# https://www.hackerrank.com/challenges/ctci-balanced-brackets?h_r=next-challenge&h_v=zen

def is_matched(expression):
  stack = []
  for letter in expression:
    if is_opener(letter):
      stack.append(letter)
    else:
      if len(stack) == 0:
        return False
      preceding_letter = stack.pop()
      if not is_pair(preceding_letter, letter):
        return False
  return len(stack) == 0

def is_pair(first, last):
  pairs = {
    '{': '}',
    '[': ']',
    '(': ')'
  }
  return last == pairs[first]

def is_opener(letter):
  return letter in ["[","(","{"]

f = open('input.txt','r')
t = int(f.readline().strip())
for a0 in range(t):
    expression = f.readline().strip()
    if is_matched(expression) == True:
        print("YES")
    else:
        print("NO")

