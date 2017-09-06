# pylint: skip-file
# https://www.hackerrank.com/challenges/ctci-find-the-running-median?h_r=next-challenge&h_v=zen
class Heap:
  
  def __init__(self, is_max=False):
    self.numbers = []
    # Max heap or not
    self.is_max = is_max
    self.size = 0
  
  def get_parent_index(self, index):
    return (index - 1) // 2

  def get_parent(self, index):
    return self.numbers[self.get_parent_index(index)]  
  
  def has_parent(self, index):
    return self.get_parent_index(index) >= 0

  def get_left_child_index(self, index):
    return index*2+1

  def get_left_child(self, index):
    return self.numbers[self.get_left_child_index(index)]
  
  def get_right_child_index(self, index):
    return index*2 + 2

  def get_right_child(self, index):
    return self.numbers[self.get_left_child_index(index)]
  
  def has_right_child(self, index):
    return self.get_right_child_index(index) < len(self.numbers)
  
  def peek(self):
    if self.size == 0:
      return 0
    return self.numbers[0]
  
  def swap(self, index, other_index):
    temp1 = self.numbers[index]
    temp2 = self.numbers[other_index]
    self.numbers[index] = temp2
    self.numbers[other_index] = temp1


  # Comparing functions, depending on if it is a min or max heap
  def compare_up(self, index):
    if self.is_max:
      return self.get_parent(index) < self.numbers[index]
    else:
      return self.get_parent(index) > self.numbers[index]

  def compare_down(self, index1, index2):
    if self.is_max:
      return self.numbers[index1] > self.numbers[index2]
    else:
      return self.numbers[index1] < self.numbers[index2]
    
  def heapifyUp(self):
    index = self.size - 1
    # swap if parent is greater than child
    while self.has_parent(index) and self.compare_up(index):
      self.swap(index, self.get_parent_index(index))
      index = self.get_parent_index(index)

  def has_left_child(self, index):
    return self.get_left_child_index(index) < self.size

  # Heapify down
  def heapifyDown(self):
    index = 0
    while self.has_left_child(index):
      smaller_child_index = self.get_left_child_index(index)
      # Check if right child is smaller than left
      if self.has_right_child(index) and self.compare_down(self.get_right_child_index(index), self.get_left_child_index(index)):
        smaller_child_index = self.get_right_child_index(index)
      # Stop if parent is smaller than child
      if self.compare_down(index, smaller_child_index):
        break
      else:
        # Else swap
        self.swap(index, smaller_child_index)
      # Continue down the heap
      index = smaller_child_index
    
  def add(self, item):
    self.numbers.append(item)
    self.size += 1
    self.heapifyUp()

  # Pops the root, and reheapifies
  def poll(self):
    if self.size == 0:
      return None
    item = self.numbers[0]
    self.numbers[0] = self.numbers[-1]
    del self.numbers[-1]
    self.size -= 1
    self.heapifyDown()
    return item

  def __repr__(self):
    return str(self.numbers)
    

def get_median(min_heap, max_heap):
  if min_heap.size == max_heap.size:
    return (min_heap.peek() + max_heap.peek()) / 2
  elif min_heap.size > max_heap.size:
    return min_heap.peek()
  else:
    return max_heap.peek()


# Using a min-max-median heap for solving
f = open('/Users/hakonhukkelas/hacker_rank/cracking_the_coding_interview/Median/input.txt','r')
n = int(f.readline().strip())
min_heap = Heap(False)
max_heap = Heap( True)
median = 0
for a_i in range(n):
  item = int(f.readline().strip())
  # Adding item to either heap
  if item > median:
    min_heap.add(item)
  else:
    max_heap.add(item)
  # If size difference greater than 1, move root
  if abs(min_heap.size - max_heap.size) > 1:
    if min_heap.size > max_heap.size:
      item = min_heap.poll()
      max_heap.add(item)
    else:
      item = max_heap.poll()
      min_heap.add(item)
  median = get_median(min_heap, max_heap)
  print("{:0.1f}".format(median))

