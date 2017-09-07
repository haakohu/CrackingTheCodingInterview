# pylint: skip-file
# https://www.hackerrank.com/challenges/ctci-bfs-shortest-reach/problem
from queue import Queue
class Graph:
  
  def __init__(self, n):
    self.node_count = n
    # Only need one triangle of the matrix cos non-directional
    self.connections = [set() for y in range(n)]

  def connect(self, index1, index2):
    # Non-directional graph
    self.connections[index1].add(index2)
    self.connections[index2].add(index1)
  
  def find_all_distances(self, index):
    # BFS search
    lengths = [-1 for x in range(self.node_count)]
    lengths[index] = 0
    # FIFO queue for BFS
    queue = Queue()
    queue.put(index)
    while not queue.empty():
      current = queue.get()
      for node in self.connections[current]:
        if lengths[node] == -1: # Only update if not seen
          lengths[node] = lengths[current] + 6
          queue.put(node)
    res = [lengths[i]  for i in range(self.node_count) if i != index]
    r = ""
    for e in res:
      r += str(e) + " "
    print(r.strip())

      

f = open('input.txt','r')
t = int(f.readline())
for i in range(t):
    n,m = [int(value) for value in f.readline().split()]
    graph = Graph(n)
    for i in range(m):
        x,y = [int(x) for x in f.readline().split()]
        graph.connect(x-1,y-1) 
    s = int(f.readline())
    graph.find_all_distances(s-1)
    

