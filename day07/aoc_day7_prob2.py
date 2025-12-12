import os
from functools import cache

#Input parsing 
dir = os.path.dirname(os.path.abspath(__file__))
infile = dir+'//input.txt'
s = list(map(list, open(infile).read().split("\n")))
n, m = len(s), len(s[0])

sj = 0
for i in range(m):
    if s[0][i] == 'S':
        sj = i

# TODO : check if bfs is possible 

# Problem 2 solution using DFS + DP

@cache
def dfs(x, y):
    if x == n:
        return 1 
    if s[x][y] == '^':
        return dfs(x+1, y+1) + dfs(x+1, y-1)
    return dfs(x+1, y)

print("Answer to Problem 2 :", dfs(0, sj))

# Earlier raw non-cachable approach using only DFS

# ans = [0]
# def dfs(x, y):
#     if x == n:
#         ans[0] += 1
#         return
#     if s[x][y] == '^':
#         dfs(x+1, y+1) 
#         dfs(x+1, y-1)
#     else:
#         dfs(x+1, y)
# dfs(0, sj)
# print("Answer to Problem 2 :", ans[0])


