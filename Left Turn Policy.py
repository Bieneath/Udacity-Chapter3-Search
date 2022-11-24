# ----------
# User Instructions:
# 
# Implement the function optimum_policy2D below.
#
# You are given a car in grid with initial state
# init. Your task is to compute and return the car's 
# optimal path to the position specified in goal; 
# the costs for each motion are as defined in cost.
#
# There are four motion directions: up, left, down, and right.
# Increasing the index in this array corresponds to making a
# a left turn, and decreasing the index corresponds to making a 
# right turn.
import heapq
from heapq import heappush, heappop

forward = [[-1,  0], # go up
           [ 0, -1], # go left
           [ 1,  0], # go down
           [ 0,  1]] # go right
forward_name = ['up', 'left', 'down', 'right']

# action has 3 values: right turn, no turn, left turn
action = [-1, 0, 1]
action_name = ['R', '#', 'L']

# EXAMPLE INPUTS:
# grid format:
#     0 = navigable space
#     1 = unnavigable space 
grid = [[1, 1, 1, 0, 0, 0],
        [1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1]]

init = [4, 3, 0] # given in the form [row,col,direction]
                 # direction = 0: up
                 #             1: left
                 #             2: down
                 #             3: right
                
goal = [2, 0] # given in the form [row,col]

cost = [2, 1, 20] # cost has 3 values, corresponding to making 
                  # a right turn, no turn, and a left turn

# EXAMPLE OUTPUT:
# calling optimum_policy2D with the given parameters should return 
# [[' ', ' ', ' ', 'R', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', '#'],
#  ['*', '#', '#', '#', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', ' '],
#  [' ', ' ', ' ', '#', ' ', ' ']]
# ----------

# ----------------------------------------
# modify code below
# ----------------------------------------
class Cell:
    '''
    i, j, direction, cost, action, previous cell
    '''
    def __init__(self, i, j, d, cost=0, action='#', prev=None):
        self.i = i
        self.j = j
        self.d = d
        self.cost = cost
        self.action = action
        self.prev = prev # link to previous cell
        self.idx = [self.cost, self.i, self.j, self.d]
    def __lt__(self, other): # comparison between Cells
        return self.idx < other.idx

def optimum_policy2D(grid,init,goal,cost):
    m, n = len(grid), len(grid[0])
    # initial policy2D matrix
    policy2D = [[' '] * n for _ in range(m)]
    i_x, i_y, i_d = init
    # format for each cell:
    # i, j, direction, cost, action, previous_cell
    start = Cell(i_x, i_y, i_d, 0, '#', None)
    seen = {(i_x, i_y, i_d)}
    hq = [start]
    while hq:
        cell = heappop(hq)
        cur_cost, i, j, d = cell.idx
        if i == goal[0] and j == goal[1]: # reach the goal
            policy2D[i][j] = '*'
            while cell.prev:
                act = cell.action
                prev = cell.prev
                policy2D[prev.i][prev.j] = act
                cell = prev
            break
        for k, t in enumerate(action): # 0:right, 1:forward, 2:left
            new_d = d + t # new direction idx
            di, dj = forward[new_d%4] # new direction increment
            u, v = i + di, j + dj
            if 0 <= u < m and 0 <= v < n and not grid[u][v] and (u, v, new_d) not in seen:
                new_cost = cur_cost + cost[k]
                # i, j, direction, cost, action, previous_cell
                new_cell = Cell(u, v, new_d, new_cost, action_name[k], cell)
                heappush(hq, new_cell)
                seen.add((u, v, new_d))

    return policy2D

# # test
# ret = optimum_policy2D(grid, init, goal, cost)
# for line in ret:
#     print(line)
