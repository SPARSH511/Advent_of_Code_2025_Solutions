import os

# Input parsing
dir = os.path.dirname(os.path.abspath(__file__))
infile = dir+'//input.txt'
s = open(infile).read().split("\n")

# Modifications in the input to preserve the whitespaces associated with each value
max_len = max(len(line) for line in s)
padded_lines = [line.ljust(max_len) for line in s]
columns_chars = list(zip(*padded_lines))
result = []
current_col = []
for col in columns_chars:
    if any(c != ' ' for c in col):  
        current_col.append(col)
    elif current_col:  
        col_values = [''.join(row) for row in zip(*current_col)]
        max_width = max(len(val.rstrip()) for val in col_values)
        col_values = [val[:max_width] for val in col_values]
        result.append(col_values)
        current_col = []
if current_col: 
    col_values = [''.join(row) for row in zip(*current_col)]
    max_width = max(len(val.rstrip()) for val in col_values)
    col_values = [val[:max_width] for val in col_values]
    result.append(col_values)

# Problem 2 solution
transpose = []
for j in range(len(result)):
    row = []
    for i in range(len(result[0])):
        row.append(result[j][i])
    transpose.append(row)

ans = 0
for row in transpose:
    op = row[-1].strip()
    row_ans = 1

    for j in range(len(row[0])):
        curr = ''
        for i in range(len(row)-1):
            if row[i][j] == ' ': continue
            curr += row[i][j]
        if op == '*': row_ans *= int(curr)       
        else: row_ans += int(curr)

    if op == '+': row_ans -= 1
    ans += row_ans


print("Answer to Problem 2:", ans)
 

               
