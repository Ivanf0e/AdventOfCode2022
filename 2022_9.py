import csv
# 1. all unique pos of T. T follows H. H follows directions.
# 2. 

# ds = [['R', 4],
#         ['U', 4],
#         ['L', 3],
#         ['D', 1],
#         ['R', 4],
#         ['D', 1],
#         ['L', 5],
#         ['R', 2]]
ds = []
with open('2022_9_input.csv', 'r') as f:
    reader = csv.reader(f)
    for i, row in enumerate(reader):
        ds += [[row[0][0], int(row[0][2:])]]
def sgn(a):
    return 1 if a > 0 else -1
sc1, H, T, Ha, Ta = 0, [0,0], [0,0], [], [] # start coordinates
# vis = [[0 for j in range(6)] for i in range(6)]
for d in ds:
    if d[0] == 'R': a, b = 1, 1
    elif d[0] == 'L': a, b = 1, -1
    elif d[0] == 'U': a, b = 0, 1
    elif d[0] == 'D': a, b = 0, -1
    for k in range(abs(d[1])):
        H[a] += b
        dHT = [H[0] - T[0], H[1] - T[1]]
        if abs(dHT[0]) == 2:
            T[0] += sgn(dHT[0])
            T[1] += dHT[1]
        elif abs(dHT[1]) == 2:
            T[1] += sgn(dHT[1])
            T[0] += dHT[0]
        Ha += H
        if T not in Ta: sc1 += 1 # 6018
#         vis[T[0]][T[1]] = 1
        Ta += [[T[0], T[1]]]
#         print(H, T)

TaT = [[row[i] for row  in Ta] for i in range(len(Ta[0]))]
Tr = [min(TaT[1]), max(TaT[1]), min(TaT[0]), max(TaT[0])]
# print(Ta)
# [print(v) for v in vis]
sc2 = 0 # 383520
print(f'part1: {sc1} \npart2: {sc2} ')
print(f'T range is {Tr}')