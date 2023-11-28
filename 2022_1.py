import csv
import re
with open('2022_1_input.csv', 'r') as f:
    reader = csv.reader(f)
    elfs, cal, calmax, calmaxi = [], 0, 0, 0
    for i, row in enumerate(reader):
        if row:
            cal += int(int(re.findall(r'\d+', row[0])[0]))
        else:
            elfs.append(cal)
            if cal > calmax:
                calmax = cal
                calmaxi = len(elfs)
            cal = 0
            #if len(elfs)==30: break
print(f'part1: {calmax} calories by elf {calmaxi}')
calmax3 = sum(sorted(elfs)[-3:])
print(f'part2: {calmax3} calories by top3')