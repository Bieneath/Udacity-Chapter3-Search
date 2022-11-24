# -----------
# User Instructions:
#
# Modify the the search function so that it returns
# a shortest path as follows:
# 
# [['>', 'v', ' ', ' ', ' ', ' '],
#  [' ', '>', '>', '>', '>', 'v'],
#  [' ', ' ', ' ', ' ', ' ', 'v'],
#  [' ', ' ', ' ', ' ', ' ', 'v'],
#  [' ', ' ', ' ', ' ', ' ', '*']]
#
# Where '>', '<', '^', and 'v' refer to right, left, 
# up, and down motions. Note that the 'v' should be 
# lowercase. '*' should mark the goal cell.
#
# You may assume that all test cases for this function
# will have a path from init to goal.
# ----------
from collections import deque

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

def search(grid,init,goal,cost):
    # ----------------------------------------
    # modify code below
    # ----------------------------------------
    if not grid or not grid[0]:
        return None
    m, n = len(grid), len(grid[0])
    
    # initial expand grid
    expand = [[' '] * n for _ in range(m)]
    
    def draw_path(path):
        for (i1, j1), (i2, j2) in zip(path, path[1:]):
            d = [i2-i1, j2-j1]
            if d == delta[0]:
                expand[i1][j1] = '^'
            elif d == delta[1]:
                expand[i1][j1] = '<'
            elif d == delta[2]:
                expand[i1][j1] = 'v'
            elif d == delta[3]:
                expand[i1][j1] = '>'
        expand[m-1][n-1] = '*'
    
    path = [init]
    dq = deque([path])
    seen = {0}
    step = 0
    while dq:
        for _ in range(len(dq)):
            path = dq.popleft()
            i, j = path[-1]
            if [i, j] == goal:
                draw_path(path)
                return expand
            for u, v in [(i, j+1), (i, j-1), (i+1, j), (i-1, j)]:
                idx = u * n + v
                if 0 <= u < m and 0 <= v < n and not grid[u][v] and idx not in seen:
                    new_path = path + [[u, v]]
                    dq.append(new_path)
                    seen.add(idx)
        step += cost
    return expand # make sure you return the shortest path

# # test
# ret = search(grid, init, goal, cost)
# for line in ret:
#     print(line)
