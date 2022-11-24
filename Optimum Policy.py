# ----------
# User Instructions:
# 
# Write a function optimum_policy that returns
# a grid which shows the optimum policy for robot
# motion. This means there should be an optimum
# direction associated with each navigable cell from
# which the goal can be reached.
# 
# Unnavigable cells as well as cells from which 
# the goal cannot be reached should have a string 
# containing a single space (' '), as shown in the 
# previous video. The goal cell should have '*'.
# ----------
from collections import deque

grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1 # the cost associated with moving from a cell to an adjacent one

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

def optimum_policy(grid,goal,cost):
    # ----------------------------------------
    # modify code below
    # ----------------------------------------
    m, n = len(grid), len(grid[0])
    i, j = goal
    # initial value matrix
    value = [[99] * n for _ in range(m)]
    value[i][j] = 0
    # initial policy matrix
    policy = [[' '] * n for _ in range(m)]
    policy[i][j] = '*'
    dq = deque([goal])
    grid[i][j] = 1
    
    while dq:
        i, j = dq.popleft()
        for k, (u, v) in enumerate([(i-1, j), (i, j-1), (i+1, j), (i, j+1)]):
            if 0 <= u < m and 0 <= v < n:
                new_cost = value[u][v] + cost
                if new_cost < value[i][j]:
                    value[i][j] = new_cost
                    policy[i][j] = delta_name[k]
                if not grid[u][v]:
                    dq.append([u, v])
                    grid[u][v] = 1

    return policy
    
# # test
# ret = optimum_policy(grid, goal, cost)
# for line in ret:
#     print(line)