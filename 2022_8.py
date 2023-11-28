import csv
import re
# 1. vissible trees, ie number in horizontal or vertical is larger
# 2. max of product of view count in each direction. 

# trees = [[3,0,3,7,3],
#         [2,5,5,1,2],
#         [6,5,3,3,2],
#         [3,3,5,4,9],
#         [3,5,3,9,0]]
trees = []
with open('2022_8_input.csv', 'r') as f:
    reader = csv.reader(f)
    for i, row in enumerate(reader):
        trees += [[int(e) for e in row[0]]]
col, row = len(trees[0]), len(trees)

vis = [[0 for j in range(col)] for i in range(row)]
for i in range(1, row - 1):
    tu, tb = trees[i][0], trees[i][-1]
    for j in range(1, col - 1):
        jt = col-j
        if trees[i][j] > tu:
            vis[i][j] = 1
            tu = trees[i][j]
        if trees[i][jt] > tb:
            vis[i][jt] = 1
            tb = trees[i][jt]          
for j in range(1, col - 1): # loops can be combined, but then track tl, tr over the complete loop
    tl, tr = trees[0][j], trees[-1][j]
    for i in range(1, row - 1):
        it = row-i
        if trees[i][j] > tl:
            vis[i][j] = 1
            tl = trees[i][j]
        if trees[it][j] > tr:
            vis[it][j] = 1
            tr = trees[it][j]
# [print(v) for v in vis]
sc1 = sum([sum(v) for v in vis]) + 2 * (row + col) - 4 # 1816

sc = [[1 for j in range(col)] for i in range(row)]
for i in range(0, row):
    for j in range(0,col):
        il, jl = 1, 1
        tr = trees[i][j]
        for jr in range(1,col-j):
            if tr <= trees[i][j+jr]:
                break
        for jl in range(1,j+1):
            if tr <= trees[i][j-jl]:
                break 
        for ir in range(1,row-i):
            if tr <= trees[i+ir][j]:
                break
        for il in range(1,i+1):
            if tr <= trees[i-il][j]:
                break
        sc[i][j] *= jr * jl * ir * il
# [print(v) for v in sc]

sc2 = max([max(v) for v in sc]) # 383520
print(f'part1: {sc1} \npart2: {sc2} ')