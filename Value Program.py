# ----------
# User Instructions:
# 
# Create a function compute_value which returns
# a grid of values. The value of a cell is the minimum
# number of moves required to get from the cell to the goal. 
#
# If a cell is a wall or it is impossible to reach the goal from a cell,
# assign that cell a value of 99.
# ----------
from collections import deque

grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1 # the cost associated with moving from a cell to an adjacent one

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

def compute_value(grid,goal,cost):
    # ----------------------------------------
    # insert code below
    # ----------------------------------------
    m, n = len(grid), len(grid[0])
    value = [[99] * n for _ in range(m)]
    value[goal[0]][goal[1]] = 0
    dq = deque([goal])
    grid[goal[0]][goal[1]] = 1
    
    while dq:
        i, j = dq.popleft()
        for u, v in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if 0 <= u < m and 0 <= v < n:
                value[i][j] = min(value[i][j], value[u][v] + cost)
                if not grid[u][v]:
                    dq.append([u, v])
                    grid[u][v] = 1
    # make sure your function returns a grid of values as 
    # demonstrated in the previous video.
    return value 
    
# # test
# ret = compute_value(grid, goal, cost)
# for line in ret:
#     print(line)