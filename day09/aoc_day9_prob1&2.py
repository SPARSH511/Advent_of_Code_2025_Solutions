import os

#Input parsing 
dir = os.path.dirname(os.path.abspath(__file__))
infile = dir+'//input.txt'
s = open(infile).read().split("\n")
s = [tuple(map(int,row.split(','))) for row in s]
n = len(s)

# Problem 1 solution

max_area = -1
for i in range(n-1):
    for j in range(i+1, n):
        max_area = max(max_area, (abs(s[i][1]-s[j][1])+1) * (abs(s[i][0]-s[j][0])+1))

print("Answer to Problem 1 :", max_area)

# Problem 2 solution

# A rectangle is valid if and only if none of the red tile connections cross through it

max_area = -1
for i in range(n-1):
    for j in range(i+1, n):
        p1, p2 = s[i], s[j]
        area = (abs(p1[1]-p2[1])+1) * (abs(p1[0]-p2[0])+1)

        # If the area is less than or equal to current max_area then no point in checking it further
        if area <= max_area: continue

        # Boundaries of the current rectangle chosen
        xmin, xmax, ymin, ymax = min(p1[0], p2[0]), max(p1[0], p2[0]), min(p1[1], p2[1]), max(p1[1], p2[1])

        # Checking by taking the edges one by one by considering the consecutively close points
        # if they lie completely inside our current rectangle taken by choosing two opposite corners

        validity = True
        for indx in range(n):
            nxt_indx = (indx+1) % n
            x1, y1 = s[indx]
            x2, y2 =  s[nxt_indx]

            if not (
                (x1 >= xmax and x2 >= xmax)
                or (x1 <= xmin and x2 <= xmin)
                or (y1 >= ymax and y2 >= ymax)
                or (y1 <= ymin and y2 <= ymin)
            ):
                validity = False
                break

        if validity: max_area = area

print("Answer to Problem 2 :", max_area)

