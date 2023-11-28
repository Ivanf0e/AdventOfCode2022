import csv
# 1. first instance 4 unique characters
# 2. 
with open('2022_6_input.csv', 'r') as f:
    reader = csv.reader(f)
    for i, row in enumerate(reader):
        if row:
            r = row[0]
# r='mjqjpqmgbljsphdztnvjfqwrcgsmlb'

n = [4, 14]
for n0 in n:
    for i in range(len(r)):
        if len(set(r[i:i+n0])) == n0:
            print(f'part{n0}: {i + n0} at string {r[i:i+n0]}')
            break
#     if i == 10: break