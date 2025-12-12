import os

#Input parsing 
dir = os.path.dirname(os.path.abspath(__file__))
infile = dir+'//input.txt'
s = open(infile).read().split("\n\n")

presents, info = s[:-1], s[-1]

# More of an approximation problem seriously, and for some people even though the code doesn't pass for 
# sample case it passes for the actual input

l = len(presents)
while l:
    p = presents.pop(0)
    presents.append(p.split(":")[1].count('#'))
    l-=1

info = [(tuple(map(int, row.split(": ")[0].split('x'))), 
         tuple(map(int,row.split(": ")[1].split()))) 
         for row in info.split('\n')]

ans = 0
for grid in info:
    # Take 15% more area than required for each present and it is solved [subreddit code had 20% more :)]
    if grid[0][0] * grid[0][1] >= sum(grid[1][i] * presents[i] * 1.15 for i in range(len(grid[1]))):
        ans += 1


print("Answer to Problem 1 :", ans)
