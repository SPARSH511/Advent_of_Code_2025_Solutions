import os

#Input parsing 
dir = os.path.dirname(os.path.abspath(__file__))
infile = dir+'//input.txt'
s = list(map(list, open(infile).read().split("\n")))
n, m = len(s), len(s[0])

# Finding the start point's j coordinate in first row ('S')
sj = 0
for j in range(m):
    if s[0][j] == 'S':
        sj = j
        break

# Problem 1 solution
    
# Main Logic [we remove the current point's j coordinate part which was considered for splitting and 
# add its left and right neighbours'j coordinate parts which will be considered in the same way and 
# we count the splits in between] 

start_flag = False
splitters = set()
splits = 0

for i in range(1, n):
    if start_flag:
        addition_set, removal_set = set(), set()
        for split_point in splitters:
            if s[i][split_point] == '^':
                splits += 1
                addition_set.add(split_point-1)
                addition_set.add(split_point+1)
                removal_set.add(split_point)
        for point in removal_set:
            splitters.remove(point)
        splitters = splitters.union(addition_set)
    else:
        if s[i][sj] == '^':
            start_flag = True
            splits += 1
            splitters.add(sj+1)
            splitters.add(sj-1)

print("Answer to Problem 1 :",splits)






