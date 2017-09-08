#!/bin/python3
# pylint: skip-file
# https://www.hackerrank.com/challenges/ctci-linked-list-cycle/problem
"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


def has_cycle(head):
  if head == None:
    return False
  slow = head
  fast = head.next
  # If there is a loop, the fast will catch up to the slow exactly at the second loop.
  while slow != fast:
    if fast == None or fast.next == None:
      return False
    slow = slow.next
    fast = fast.next.next
  return True
    

