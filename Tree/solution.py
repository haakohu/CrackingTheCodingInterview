
# pylint: skip-file
# https://www.hackerrank.com/challenges/ctci-is-binary-search-tree/problem
from math import inf
class node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

    
def checkBST(root):
  return check_recursive(root, -inf, inf)

def check_recursive(root, minV, maxV):
  if not root:
    return True
  if not minV < root.data < maxV:
    return False
  if not check_recursive(root.left, minV, root.data):
    return False
  if not check_recursive(root.right, root.data, maxV):
    return False
  return True


  

root = node(4)
root.left = node(2)
root.right = node(6)
root.left.left = node(1)
root.left.right = node(3)
root.right.left = node(5)
root.right.right = node(7)
assert(checkBST(root))