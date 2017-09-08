#!/bin/python3
# pylint: skip-file
# https://www.hackerrank.com/challenges/ctci-merge-sort/problem

def mergesort(array):
  start = 0
  end = len(array)-1
  clone = [x for x in array]
  swaps = mergesort_rec(array,start,end, clone)
  return swaps

def mergesort_rec(array, left_start, right_end, clone):
  # No more elements
  if left_start >= right_end:
    return 0
  mid = (left_start + right_end) // 2
  left_end = mid
  right_start = mid +1
  swaps = 0
  swaps += mergesort_rec(array, left_start, left_end, clone)
  swaps += mergesort_rec(array, right_start, right_end, clone)
  return swaps + merge_halves(array, left_start,mid, right_end, clone)

# Til og med right end
def merge_halves(array,left_start, mid, right_end, clone):
  #print("merge_halves",array, left_start, right_end)
  swaps = 0
  left = left_start
  index = left_start
  right = mid +1 
  while left <= mid or right <= right_end:
    if left > mid:
      array[index] = clone[right]
      index += 1
      right += 1
    elif right > right_end:
      array[index] = clone[left]
      index += 1
      left += 1
    elif clone[left] <= clone[right]:
      array[index] = clone[left]
      index += 1
      left += 1
    else:
      array[index] = clone[right]
      index += 1
      right += 1
      swaps += mid + 1 - left
  return swaps

#!/bin/python3

import sys

def countInversions(arr):
    return mergesort(arr)


if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        arr = list(map(int, input().strip().split(' ')))
        result = countInversions(arr)
        print(result)

