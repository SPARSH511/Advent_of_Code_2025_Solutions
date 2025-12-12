import os
from scipy.optimize import linprog


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

# It is a Linear Programming Problem (read on scipy official docs)

def solver(row):
    _, buttons, target = row
       
    buttons_matrix = []
    for button in buttons:
        r = [0]*len(target)
        for i in button:
            r[i] = 1
        buttons_matrix.append(r)

    coeffs = [1]*len(buttons_matrix) # coeff's of linear obj function to minimize 
                                     # (this is all 1's coz all the buttons have the same cost)

    x = linprog(c = coeffs, A_eq = list(zip(*buttons_matrix)), b_eq = target, integrality = True).fun

    return x

ans = 0
for row in s:
    ans += solver(row)

print("Answer to Problem 2 :", int(ans))

