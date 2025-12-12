import os

# Input parsing
dir = os.path.dirname(os.path.abspath(__file__))
infile = dir+"\\input.txt"
s = open(infile).read().strip().split("\n")

# Problem 1 solution (O(NO. OF COMMANDS))
def problem1():
    curr_state, ans = 50, 0
    for command in s:
        direction, value = command[0], int(command[1:])
        if direction == 'R':
            curr_state += value
        else:
            curr_state -= value
        curr_state %= 100
        if curr_state == 0:
            ans += 1
    return ans

# Problem 2 solution (O(NO. OF COMMANDS * SUM OF COMMAND VALUES WHERE OPERATION IS 'L'))
def problem2():
    curr_state, ans = 50, 0
    for command in s:
        direction, value = command[0], int(command[1:])
        if direction == 'R':
            curr_state += value
            if curr_state >= 100:
                ans += curr_state // 100
        else:
            # Had to do brute force here because I am at my wit's end (STILL EXECUTED INSTANTLY THOUGH !)
            for _ in range(value):
                curr_state -= 1
                curr_state %= 100
                if curr_state == 0:
                    ans += 1
        curr_state %= 100
    return ans


print("Answer to Problem 1:", problem1())
print("Answer to Problem 2:", problem2())