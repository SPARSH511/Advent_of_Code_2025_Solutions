import os
from collections import deque

#Input parsing 
dir = os.path.dirname(os.path.abspath(__file__))
infile = dir+'//input.txt'
s = open(infile).read().split("\n")
s = [row.split() for row in s]

def custom_changer(item):
    item = item.lstrip('(').rstrip(')')
    item = tuple(map(int, item.split(',')))
    return item

s = [[
        row[0].lstrip('[').rstrip(']'), 
        list(map(custom_changer, row[1:-1])), 
        tuple(map(int, row[-1].rstrip('}').lstrip('{').split(',')))
    ] for row in s]

# Problem 1 solution

def bfs(row):
    target, buttons, _ = row
    l = len(target)

    q = deque([('.'*l, 0)])
    vis = set()
    while q:
        state, clicks = q.popleft()

        if state == target:
            return clicks
        
        for button in buttons:
            curr_state = ''
            for i in range(l):
                if i in button:
                    if state[i] == '.':
                        curr_state += '#'
                    else:
                        curr_state += '.'
                else:
                    curr_state += state[i]

            if curr_state not in vis:
                q.append((curr_state, clicks + 1))                
                vis.add(curr_state)

ans = 0
for row in s:
    ans += bfs(row)

print("Answer to Problem 1 :", ans)

                
