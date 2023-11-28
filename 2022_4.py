import csv
import re
# 1. home many pairs overlapping

with open('2022_4_input.csv', 'r') as f:
    reader = csv.reader(f)
    sc1, sc2 = 0, 0
    gr = [0]*2

    for i, row in enumerate(reader):
        r = [int(e) for e in (re.findall(r'\d+', row[0]))]
        if r[0] <= r[2] and r[1] >= r[3]: sc1 += 1 # overlapping
        elif r[0] >= r[2] and r[1] <= r[3]: sc1 += 1
        if not(r[1] < r[2] or r[0] > r[3]): sc2 += 1 # overlapping partially       
#         print(r, sc1)
#         if i == 10: break

print(f'part1: {sc1} points')
print(f'part2: {sc2} points')