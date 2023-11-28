import csv
# 1. sum of signal strength (x * c) at cycles cc, while x is changed by cmd 'addx'
X, cc, c = [1], list(range(20,221,40)), 0
# 2. what is written for pixels if pixel at c in row overlaps sprite at pos X, X+1, X+2, for multiple col(umns)
row, col = 6, 40
crt = '' # [[0 for j in range(col)] for i in range(row)]
sp, spd = [0, 1, 2], [-1, 0, 1] # sprite location and its default

with open('2022_10_input.csv', 'r') as f:
    reader = csv.reader(f)
    for k, row in enumerate(reader):
        crt += '#' if c in sp else '.'
        X += [X[-1]]
#         print(c, X[-1], sp, crt)
        c = (c + 1) % 40
        
        if row[0][0] == 'a': # add to x after 2 cycles (c). to do: make one function
            crt += '#' if c in sp else '.'
            X += [X[-1] + int(row[0][5:])]
            sp = [e + X[-1] for e in spd]
#             print(c, X[-1], sp, crt)
            c = (c + 1) % 40
      
#         if k == 10: break
[print(crt[i:i+col]) for i in range(0,240,col)]        
sc1 = sum([X[e-1] * e for e in cc]) # 12740
sc2 = 'RBPARAGF'
# [print(r) for r in crt]
print(f'part1: {sc1} \npart2: {sc2} ') # check that part is ok for HT[1]