import os 

#Input parsing 
dir = os.path.dirname(os.path.abspath(__file__))
infile = dir+'//input.txt'
ranges, queries = open(infile).read().strip().split("\n\n")

ranges = [tuple(map(int, rg.split('-'))) for rg in ranges.split('\n')]
queries = [int(query) for query in queries.split('\n')]

# Merges the ranges 
def merge_ranges(ranges):
    if not ranges:
        return []
    ranges.sort()
    merged = [ranges[0]]
    for start, end in ranges[1:]:
        if start <= merged[-1][1]:  # Overlapping
            merged[-1] = (merged[-1][0], max(merged[-1][1], end))
        else:
            merged.append((start, end))
    return merged

# Binary search on merged ranges list
def is_in_range(num, merged_ranges):
    left, right = 0, len(merged_ranges) - 1
    while left <= right:
        mid = (left + right) // 2
        start, end = merged_ranges[mid]
        if start <= num <= end:
            return True
        elif num < start:
            right = mid - 1
        else:
            left = mid + 1
    return False

merged = merge_ranges(ranges)

# Problem 1
count = 0
for query in queries:
    if is_in_range(query, merged):
        count += 1

# Problem 2
total_members = sum(end - start + 1 for start, end in merged)

print("Answer for Problem 1:", count)
print("Answer for Problem 2:", total_members)

