import csv
import re
# 1. home many pairs overlapping

with open('2022_5_input.csv', 'r') as f:
    reader = csv.reader(f)
    sc2 = 0
    cr = []

    for i, row in enumerate(reader):
        if row:
            r0 = row[0]
            if r0[0] == '[': # all stacks
                cr += [[r0[i] for i in range(1,len(r0),4)]] # step of 4 hardcoed in input
            elif r0[0] == ' ': # finished stacks
                d, w = len(cr), len(cr[0])
                crt = [[row[j] for row  in cr] for j in range(w)]
                crb = [[crtr[j] for j in range(d-1,-1,-1) if crtr[j] != ' '] for crtr in crt]
                cr2 = [[e for e in row] for row in crb] # deepcopy
            else: # instructions to move
                r = [int(e) for e in re.findall(r'\d+', r0)]
                for j in range(r[0]):
                    crb[r[2]-1].append(crb[r[1]-1].pop())
                cr2[r[2]-1] += cr2[r[1]-1][-r[0]:]
                cr2[r[1]-1] = cr2[r[1]-1][0:-r[0]]
#         if i == 11: break
sc1 = ''.join([e[-1] for e in crb])
sc2 = ''.join([e[-1] for e in cr2])

print(f'part1: {sc1}')
print(f'part2: {sc2}')