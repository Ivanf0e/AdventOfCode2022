import csv
# 1. all unique pos of T. T follows H. H follows directions.
# 2. same but for 9 Ts and last T's unique positions.

dictd = { # coordinate system
    'R': [1, 1],
    'L': [1, -1],
    'U': [0, 1],
    'D': [0, -1]}

ds = []
with open('2022_9_input.csv', 'r') as f:
    reader = csv.reader(f)
    for i, row in enumerate(reader):
        ds += [dictd[row[0][0]] + [int(row[0][2:])]]

def sgn(a):
    return 1 if a > 0 else -1
sc1, sc2, HT, Ha, T1, T9, = 0, 0, [[0,0] for _ in range(10)], [], [], [] # start coordinates
HT2,stop=[[0,0] for _ in range(10)], False
for d in ds:
#     if d == ds[2]: break
#     a, b = d[0], d[1]
    for k in range(abs(d[2])):
        HT[0][d[0]] += d[1]
        HT2[0][d[0]] += d[1]
        for i in range(1,10):
            dHT = [HT[i-1][0] - HT[i][0], HT[i-1][1] - HT[i][1]]
            # to do track relative move instead of absolute coordinates 
            dHTa = sum([e*e for e in dHT])
            
            if dHTa <= 2: # no move, and subsequent tails should also remain still
                break
            elif dHTa == 4: #lateral move
                xy = 0 if dHT[0] else 1 # move direction not always in direction of head
                HT[i][xy] += sgn(dHT[xy])
            elif dHTa >= 5: # diagonal
                HT[i][0] += sgn(dHT[0])
                HT[i][1] += sgn(dHT[1])
            else:
                print('?') #2678
                
                     
#             if abs(dHT[0]) == 2:
#                 if abs(dHT[1]) == 2: # case that they move diagonally both
#                     HT[i][0] += sgn(dHT[0])
#                     HT[i][1] += sgn(dHT[1])
#                 else:
#                     HT[i][0] += sgn(dHT[0])
#                     HT[i][1] += dHT[1]
#             elif abs(dHT[1]) == 2:
#                 HT[i][1] += sgn(dHT[1])
#                 HT[i][0] += dHT[0]
#             if HT!=HT2: stop = True; break
        if HT[1] not in T1: sc1 += 1 # 6018
        if HT[-1] not in T9: sc2 += 1 # 2619
        T1 += [[HT[1][0], HT[1][1]]]
        T9 += [[HT[-1][0], HT[-1][1]]]
#     if stop: break            
#     print(HT)

T9T = [[row[i] for row  in T9] for i in range(len(T9[0]))]
Tr = [min(T9T[1]), max(T9T[1]), min(T9T[0]), max(T9T[0])]

print(f'part1: {sc1} \npart2: {sc2} ') # check that part is ok for HT[1]
print(f'T range is {Tr}')