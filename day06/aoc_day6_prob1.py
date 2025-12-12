import os

#Input parsing 
dir = os.path.dirname(os.path.abspath(__file__))
infile = dir+'//input_sample.txt'
s = open(infile).read().split("\n")
s = [row.split() for row in s]
m, n = len(s), len(s[0])

# Problem 1 solution
ans = 0
for j in range(n):
    operator = s[m-1][j]
    col_ans = 0
    if operator == '*':
        col_ans = 1
        for i in range(m-1):
            col_ans *= int(s[i][j])
    else:
        for i in range(m-1):
            col_ans += int(s[i][j])
    ans += col_ans

print("Answer to Problem 1:", ans)






