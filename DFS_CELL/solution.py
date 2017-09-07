# pylint: skip-file
# https://www.hackerrank.com/challenges/ctci-connected-cell-in-a-grid/problem

# Returns adjacent cells
def visist_adjacent(column, row, row_count, column_count, grid):
  # List of coordinates (row, column)
  adjacent = []
  for a_row in range(max(0,row-1),min(row_count, row+2)):
    for a_column in range(max(0,column-1), min(column_count,column+2)):
      if grid[a_row][a_column] == 1:
        adjacent.append([a_row, a_column])
        grid[a_row][a_column] = 0
  return adjacent
  
def get_size(grid, column, row, row_count, column_count):
  # Not in a region
  if grid[row][column] == 0:
    return 0
  q = [[row, column]]
  count = 1
  grid[row][column] = 0
  while len(q) > 0:
    coord = q.pop()
    neighbours = visist_adjacent(coord[1], coord[0], row_count, column_count, grid)
    count += len(neighbours)
    q += neighbours
  return count

def getBiggestRegion(grid, row_count, column_count):
  # DFS search to find the biggest region
  res = 0
  for row in range(row_count):
    for column in range(column_count):
      res = max(res, get_size(grid, column, row, row_count, column_count)) 
  return res


n = int(input().strip())
m = int(input().strip())
grid = []
for grid_i in range(n):
  grid_t = list(map(int, input().strip().split(' ')))
  grid.append(grid_t)
print(getBiggestRegion(grid,n,m))

