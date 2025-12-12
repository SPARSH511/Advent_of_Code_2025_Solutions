import os

# Input parsing
dir = os.path.dirname(os.path.abspath(__file__))
infile = dir+"\\input.txt"
s = list(map(list,open(infile).read().strip().split("\n")))

m = len(s)
n = len(s[0])

def problem1():
    ans = 0
    for i in range(m):
        for j in range(n):
            count = 0
            if s[i][j] == '@':
                dir = ((0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,-1),(-1,1),(1,-1))
                for di,dj in dir:
                    if -1 < i+di < m and -1 < j+dj < n:
                        if s[i+di][j+dj] == '@': count+=1
                if count < 4:
                    ans += 1
    return ans

def clearer():
    ans = 0
    for i in range(m):
        for j in range(n):
            count = 0
            if s[i][j] == '@':
                dir = ((0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,-1),(-1,1),(1,-1))
                for di,dj in dir:
                    if -1 < i+di < m and -1 < j+dj < n:
                        if s[i+di][j+dj] == '@': count+=1
                if count < 4:
                    s[i][j] = '.'
                    ans += 1
    return ans

def problem2():
    d_ans = -1; ans = 0
    while d_ans != 0:
        d_ans = clearer()
        ans += d_ans
    return ans

print("Answer to Problem 1:",problem1())
print("Answer to Problem 2:",problem2())
