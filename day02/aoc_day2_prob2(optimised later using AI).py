from bisect import bisect_left, bisect_right
import os

# Input parsing
dir = os.path.dirname(os.path.abspath(__file__))
infile = dir+"\\input.txt"
ranges = open(infile).read().strip().split(",")
ranges = [tuple(map(int,item.split("-"))) for item in ranges]

# Problem 2 solution 
def is_invalid2(n):
    """Faster check: string is made by repeating a smaller substring > 1 times.
    
    This uses the common trick: s in (s+s)[1:-1] -> True if s is a repeated pattern.
    It's O(len(s)) and avoids building all substrings and frequencies.
    """
    s = str(n)
    if len(s) <= 1:
        return False
    # If s is multiple of a smaller substring, then s exists in (s+s)[1:-1]
    return s in (s + s)[1:-1]

def _generate_repeated_numbers(max_val):
    """Generate all integers <= max_val that are exact repetitions of a smaller substring.

    We iterate by total digit length and base-substring length (d) where total length l is
    a multiple of d and repetition count k = l // d >= 2.
    Generate patterns p in [10**(d-1), 10**d - 1] (no leading zeros), compute value int(str(p)*k).
    Use a set to deduplicate across multiple divisor decompositions.
    """
    out = set()
    max_len = len(str(max_val))
    min_len = 2  # need at least 2 repeats
    for l in range(min_len, max_len + 1):
        for d in range(1, l // 2 + 1):
            if l % d != 0:
                continue
            k = l // d
            start = 10 ** (d - 1)
            end = 10 ** d - 1
            for p in range(start, end + 1):
                val = int(str(p) * k)
                if val > max_val:
                    # values for p will only increase, so we can break
                    break
                out.add(val)
    return sorted(out)

def problem2():
    # Build a single list of all repeated numbers up to the largest high bound
    max_high = max(high for low, high in ranges)
    repeated_nums = _generate_repeated_numbers(max_high)
    # prefix sums to answer range-sum queries fast
    prefix = [0]
    for val in repeated_nums:
        prefix.append(prefix[-1] + val)

    ans = 0
    for low, high in ranges:
        i = bisect_left(repeated_nums, low)
        j = bisect_right(repeated_nums, high)
        ans += prefix[j] - prefix[i]
    return ans

print("Answer to Problem 2 :",problem2())