import os
from collections import deque
from functools import cache

#Input parsing 
dir = os.path.dirname(os.path.abspath(__file__))
infile = dir+'//input.txt'
s = open(infile).read().split("\n")

# Constructing the graph using map

s = {row.split(": ")[0] : row.split(": ")[-1].split() for row in s}

# Problem 1 solution [normal BFS]

def bfs_prob1(s):
    q, vis = deque(['you']), set()
    paths = 0
    while q:
        curr = q.popleft()
        if curr == 'out':
            paths += 1
            continue
        for nbr in s[curr]:
            if (curr,nbr) or (nbr, curr) not in vis:
                vis.add((curr, nbr))
                vis.add((nbr, curr))
                q.append(nbr)
    return paths 

print("Answer to Problem 1 :", bfs_prob1(s))   

# No 'visited' set needed coz the graph is a DAG 
# Problem 2 solution [DFS + DP]

@cache
def dfs_prob2(node, fft, dac):
    if node == 'out':
        if fft and dac:
            return 1
        return 0

    paths = 0
    for nbr in s[node]:
        fft_temp, dac_temp = fft, dac
        if not fft_temp:
            if nbr == 'fft' or node == 'fft': fft_temp = True
        if not dac_temp:
            if nbr == 'dac' or node == 'dac': dac_temp = True 
        paths += dfs_prob2(nbr, fft_temp, dac_temp)

    return paths  
    

print("Answer to Problem 2 :", dfs_prob2('svr', False, False))


