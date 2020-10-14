"""
You are given a 2d grid of `"1"`s and `"0"`s that represents a "map". The
`"1"`s represent land and the `"0"s` represent water.
​
You need to write a function that, given a "map" as an argument, counts the
number of islands. Islands are defined as adjacent pieces of land that are
connected horizontally or vertically. You can also assume that the edges of the
map are surrounded by water.
​
Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
​
Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
"""
from collections import deque
​
def numIslands(grid):
    # Your code here
    counter = 0
    # we need to find 1's 
    # iterate through our matrix using a nested loop 
    for row_index, row in enumerate(grid):
        for col_index, digit in enumerate(row):
            # what happens when we see a 1? 
            if digit == "1":
                # increment our counter 
                counter += 1
                # we also need to make sure we don't double count 
                # mutate our input grid
                # if we see a 1, after we've processed it, let's just set it 0 
                grid[row_index][col_index] = 0
                # figure out how far this island extends in the 
                # horizontal and vertical directions 
                queue = deque([(row_index, col_index)])
​
                # we need to process the 1's adjacent to the current 1 
                while len(queue) > 0:
                    r, c = queue.popleft()
                    # check the 4 cardinal directions around the current 1 
                    # if we see any other 1s, add it to queue
​
                    # look north 
                    if r > 0 and grid[r-1][c] == '1':
                        grid[r-1][c] = 0
                        queue.append((r-1, c))
​
                    # look south
                    if r < len(grid) - 1 and grid[r+1][c] == '1':
                        grid[r+1][c] = 0
                        queue.append((r+1, c))
​
                    # look east 
                    if c < len(row) - 1 and grid[r][c+1] == '1':
                        grid[r][c+1] = 0
                        queue.append((r, c+1))
​
                    # look west 
                    if c > 0 and grid[r][c-1] == '1':
                        grid[r][c-1] = 0
                        queue.append((r, c-1))
​
    return counter 
                
grid1 = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
grid2 = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
​
print(numIslands(grid1))