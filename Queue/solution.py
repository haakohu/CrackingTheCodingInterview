#!/bin/python3
# pylint: skip-file
# https://www.hackerrank.com/challenges/ctci-queue-using-two-stacks/problem

class MyQueue(object):
    def __init__(self):
        self.queue = []
    
    def peek(self):
        if len(self.queue) > 0:
            return self.queue[0]
        
    def pop(self):
        if len(self.queue) > 0:
            item = self.queue[0]
            del self.queue[0]
            return item
        
    def put(self, value):
        self.queue.append(value)
        

queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])        
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())
        