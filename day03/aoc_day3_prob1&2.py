import os

# Input parsing
dir = os.path.dirname(os.path.abspath(__file__))
infile = dir+"\\input.txt"
s = open(infile).read().strip().split("\n")
m = len(s)
n = len(s[0])

# Problem 1 solution

def problem1():
    ans = 0
    for i in range(m):
        joltage = 0
        for j in range(n-1):
            for k in range(j+1, n):
                joltage = max(joltage,int(s[i][j]+s[i][k]))
        ans += joltage
    return ans


print("Answer to Problem 1:", problem1())


# # Problem 2 solution [brute force] [backtracking - doesn't work in time constraints]

# def find_largest_joltage(indx, length, curr_joltage, curr_bank):
#     if indx > n-1 or length == 12:
#         if length == 0: 
#             return 0
#         return int(curr_joltage)
    
#     pick = find_largest_joltage(indx+1, length+1, curr_joltage + curr_bank[indx], curr_bank)
#     notpick = find_largest_joltage(indx+1, length, curr_joltage, curr_bank)
    
#     return max(pick, notpick)

# def problem2():
#     ans = 0
#     for bank in s:
#         ans += find_largest_joltage(0, 0, '', bank)
#     return ans


# Problem 2 [Greedy plus Sliding Window with Recursion] 

"""
Move iteratively forward reducing the window size needed to search 
as no. of characters to be removed also gets reduced progressively.
This will also work when we only need two batteries per bank (2 chars per row)
"""

# def find_largest_joltage(bank, k):
#     if k == 0 : return ''
#     if k == len(bank) : return bank
#     win_size, max_digit, max_pos = len(bank)-k, bank[0], 0
#     for i in range(win_size+1):
#         if max_digit < bank[i]:
#             max_digit = bank[i]
#             max_pos = i
#     return max_digit + find_largest_joltage(bank[max_pos+1:], k-1)


# Problem 2 [Monotonic stack solution] 

def find_largest_joltage(digits, k):
    n = len(digits)
    if n < k:
        return digits  
    if n == k:
        return digits  
    result = []
    to_remove = n - k
    for digit in digits:
        while result and to_remove > 0 and result[-1] < digit:
            result.pop()
            to_remove -= 1
        result.append(digit)
    return ''.join(result[:k])

def problem2():
    ans = 0
    for bank in s:
        ans += int(find_largest_joltage(bank, 12))
    return ans

print("Answer to Problem 2:", problem2())


