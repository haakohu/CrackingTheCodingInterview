#!/bin/python3
# pylint: skip-file
# https://www.hackerrank.com/challenges/ctci-comparator-sorting/problem
from functools import cmp_to_key
class Player:
    def __init__(self, name, score):
      self.name = name
      self.score = score
    
    def __repr__(self):
      return "{0} {1}".format(self.name, self.score)
        
    def comparator(player1, player2):
      if player1.score < player2.score:
        return 1
      if player1.score > player2.score:
        return -1
      if player1.name < player2.name:
        return -1
      if player1.name > player2.name:
        return 1
      return 0
        
      
        
        

