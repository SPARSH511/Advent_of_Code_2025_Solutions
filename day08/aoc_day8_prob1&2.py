import os
from heapq import heappush, heappop, nlargest
from math import prod
from collections import defaultdict

#Input parsing 
dir = os.path.dirname(os.path.abspath(__file__))
infile = dir+'//input.txt'
s = open(infile).read().split("\n")
s = [tuple(map(int,row.split(','))) for row in s]
n = len(s)

def euclidean_dist(p1, p2):
    x1,y1,z1 = p1
    x2,y2,z2 = p2
    return ((x1-x2)**2 +(y1-y2)**2 + (z1-z2)**2)**0.5

def make_heap():
    heap = []
    for i in range(n):
        for j in range(i+1, n):
            heappush(heap, (euclidean_dist(s[i], s[j]), s[i], s[j]))
    return heap

def custom_filler(): return -1

def calculate(heap, req_num_pairs, req_num_largest = 0):
    circuits, box_to_cir_id, new_circuit_id = {}, defaultdict(custom_filler), 0
    pairs = 0
    last_pair_added = tuple()

    while pairs < req_num_pairs:
        _, p1, p2 = heappop(heap)
        
        p1_id = box_to_cir_id[p1]
        p2_id = box_to_cir_id[p2]

        if p1_id == -1 and p2_id != -1:
            circuits[p2_id].add(p1)
            box_to_cir_id[p1] = p2_id 
            last_pair_added = (p1, p2)

        elif p2_id == -1 and p1_id != -1:
            circuits[p1_id].add(p2)
            box_to_cir_id[p2] = p1_id
            last_pair_added = (p1, p2)
        
        elif p1_id != -1 and p2_id != -1:
            if p1_id != p2_id:
                circuits[p1_id] = circuits[p1_id].union(circuits[p2_id]) # Merge the two circuits if both of the boxes lie in one of the circuits
                for box in circuits[p2_id]:
                    box_to_cir_id[box] = p1_id
                last_pair_added = (p1, p2)
                del circuits[p2_id] # Remove that box's circuit whose elements were merged with the other box's circuit
        
        else:
            new_circuit_id += 1
            circuits[new_circuit_id] = set([p1, p2])
            box_to_cir_id[p1] = new_circuit_id   
            box_to_cir_id[p2] = new_circuit_id
            last_pair_added = (p1, p2)

        pairs += 1
    
    larg_cir_ids = nlargest(req_num_largest, circuits, key = lambda x : len(circuits[x]))

    return circuits, larg_cir_ids, last_pair_added


# Problem 1 solution

circuits, larg_cir_ids, _ = calculate(make_heap(), 1000, 3)
print("Answer to Problem 1 :",prod(len(circuits[cir_id]) for cir_id in larg_cir_ids))

# Problem 2 solution

heap = make_heap()
_, _, last_pair_added = calculate(heap, len(heap))
print("Answer to Problem 2 :", last_pair_added[0][0]*last_pair_added[1][0])