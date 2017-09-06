# pylint: skip-file
# https://www.hackerrank.com/challenges/ctci-contacts?h_r=next-challenge&h_v=zen

class Node:
  
  def __init__(self, data):
    self.data = data
    # Using array as hackerrank ran out of memory with dictionary
    self.children = []
    self.leaf = False
    # Count of leaf nodes
    self.count = 0

  def get_child(self, char):
    for child in self.children:
      if child.data == char:
        return child
    return None
  
def solve(op, word, root):
  res = None
  if op == 'add':
    add(word,root)
  else:
    res = find(word, root)
    print(res)


def find(word, root):
  for char in word:
    child = root.get_child(char)
    if not child:
      return 0
    root = child
  return root.count
  
  
def add(word, root):
  for letter in word:
    child = root.get_child(letter)
    if not child:
      child = Node(letter)
      root.children.append(child)
    root.count += 1
    root = child
  root.count += 1
  root.leaf = True

f = open('input.txt','r')
root = Node(None)
f.readline()
for line in f.readlines():
  op, contact = line.strip().split(' ')
  solve(op, contact, root)

