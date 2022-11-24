# -----------
# User Instructions:
#
# Modify the the search function so that it becomes
# an A* search algorithm as defined in the previous
# lectures.
#
# Your function should return the expanded grid
# which shows, for each element, the count when
# it was expanded or -1 if the element was never expanded.
# 
# If there is no path from init to goal,
# the function should return the string 'fail'
# ----------
from collections import deque
import bisect
import heapq
import platform

# print(platform.python_version())

grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]
heuristic = [[9, 8, 7, 6, 5, 4],
             [8, 7, 6, 5, 4, 3],
             [7, 6, 5, 4, 3, 2],
             [6, 5, 4, 3, 2, 1],
             [5, 4, 3, 2, 1, 0]]

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

def search(grid,init,goal,cost,heuristic):
    # ----------------------------------------
    # modify the code below
    # ----------------------------------------
    if not grid or not grid[0]: 
        return None
    m, n = len(grid), len(grid[0])
    
    expand = [[-1] * n for _ in range(m)]
    i, j = init
    value = 0 + heuristic[i][j]
    # dq = deque([[value, i, j]])
    queue = [[value, i, j]]
    seen = {i * n + j}
    step = 0
    
    # # use normal sort function
    # while queue:
    #     value, i, j = queue.pop()
    #     expand[i][j] = step
    #     step += cost
    #     if [i, j] == goal:
    #         return expand
    #     pre_step = value - heuristic[i][j]
    #     for u, v in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
    #         idx = u * n + v
    #         if 0 <= u < m and 0 <= v < n and not grid[u][v] and idx not in seen:
    #             new_value = pre_step + cost + heuristic[u][v]
    #             # bisect.insort(dq, [new_value, u, v])
    #             queue.append([new_value, u, v])
    #             seen.add(idx)
    #     queue.sort(reverse=True)
    
    # use heapq function
    while queue:
        value, i, j = heapq.heappop(queue)
        expand[i][j] = step
        step += cost
        if [i, j] == goal:
            return expand
        pre_step = value - heuristic[i][j]
        for u, v in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            idx = u * n + v
            if 0 <= u < m and 0 <= v < n and not grid[u][v] and idx not in seen:
                new_value = pre_step + cost + heuristic[u][v]
                heapq.heappush(queue, [new_value, u, v])
                seen.add(idx)
    return 'fail'

# # test  
# ret = search(grid, init, goal, cost, heuristic)
# for line in ret:
#     print(line)
#     print('\n')