#/usr/bin/python3
# pylint: skip-file
# https://www.hackerrank.com/challenges/ctci-array-left-rotation

def solve(N, d, elements):

  # Do d shifts to left 
  # Only need rest of d from n
  shifts = d % N
  moving = elements[0:shifts]
  return elements[shifts::] + moving

def solve_from_file(fname):
  f = open(fname + '_input.txt','r')

  N, d = [int(x) for x in f.readline().split(" ")]
  elements = [int(x) for x in f.readline().split(" ")]

  return solve(N, d, elements)


sample_solution = solve_from_file("sample")
assert(sample_solution  == [5,1,2,3,4])

