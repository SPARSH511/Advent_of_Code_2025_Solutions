import os
from collections import defaultdict

# Input parsing
dir = os.path.dirname(os.path.abspath(__file__))
infile = dir+"\\input.txt"
s = open(infile).read().strip().split(",")
s = [tuple(map(int,item.split("-"))) for item in s]

# Problem 1 solution

def is_invalid1(n):
    str_n = str(n)
    for i in range(len(str_n)//2+1):
        if str_n[:i] == str_n[i:]:
            return True
    return False

def problem1():
    ans = 0
    for low, high in s:
        for n in range(low, high + 1):
            if is_invalid1(n):
                ans += n
    return ans

# Problem 2 solution 

""" Using map (brute force) [O(N * L^2) where L is number of digits in n] """
# def is_invalid2(n):
#     str_n = str(n)
#     l, subs_freq = len(str_n), defaultdict(int) 
#     for i in range(l):
#         for j in range(i+1, l+1):
#             subs_freq[str_n[i:j]] += 1
#     for subs, freq in subs_freq.items():
#         if freq * subs == str_n and freq > 1:
#             return True
#     return False

""" Trick optimisation for Problem 2 solution [O(N * L)] """
def is_invalid2(n):
    str_n = str(n)
    if len(str_n) <= 1:
        return False
    # If s is multiple of a smaller substring, then s exists in (s+s)[1:-1]
    return str_n in (str_n + str_n)[1:-1]

def problem2():
    ans = 0
    for low, high in s:
        for n in range(low, high + 1):
            if is_invalid2(n):
                ans += n
    return ans

print("Answer to Problem 1 :",problem1())
print("Answer to Problem 2 :",problem2())