import csv
import string
import matplotlib.pyplot as plt
# 1. min steps (hor or ver) from S to E when height difference is <= 1 letter
# 2. start pos at a when min steps in minimal over all strat pos (only b in 2nd column so start in first column)


hdict = dict(zip(list(string.ascii_lowercase), list(range(26))))
hdict['S'], hdict['E'], h, hinf = 0, 25, [], 1000000

with open('2022_12_input.csv', 'r') as f:
    reader = csv.reader(f)
    for k, row in enumerate(reader):
        if row:
            h += [[hdict[e] for e in row[0]]]
            if 'S' in row[0]: S = [k, row[0].index('S')]
            if 'E' in row[0]: E = [k, row[0].index('E')]
            
S = [19,0] # last one in puzzle 1, [4,0] for example
row, col = len(h), len(h[0])
p = S

dr = [[1,0],[0,1],[-1,0],[0,-1]] # dir is 0 (up), 1 (right), 2 (down), 3 (left)
hv, hd = [[0 for e in row] for row in h], [[hinf for e in row] for row in h] # visited nodes and distance from start (set at very high)
hd[S[0]][S[1]] = 0 # we visit start and distance to itself 0. pn neighours TBD
pn, pd = [], [] # nodes of neighbours and distance to those
pe = []
for k in range(60000): # give coordinates and distance to neighbours
    deltah, y0, x0  = [], p[0], p[1]
    hv[y0][x0] = 1 # now visiting this node
    for dire in dr: # look in all directions
        y1, x1 = y0 + dire[0], x0 + dire[1]; p1 = [y1, x1]# y1, x1 is an unvisited neighbour
        if not(y1 <0 or y1 >= row or x1 < 0 or x1 >= col or hv[y1][x1]): # or [y1,x1] in pn
            if ((y0-y1) in [-1,0,1] and (x0-x1) in [-1,0,1]): # criterium for part 1
                dh = h[y1][x1] - h[y0][x0]
                if dh <=1: hd[y1][x1] = 1 + hd[y0][x0] # 1 up but down is possible   
            else:
                print('what?')
            if p1 in pn:
                kk = pn.index(p1)
#                 print(pd[kk], hd[y1][x1], [y1, x1])
                pd[kk] = min(pd[kk], hd[y1][x1])
            else: # pn can already be evaluated, in that case we update old value to smallest one
                pn += [p1] 
                pd += [hd[y1][x1]]
    pd0 = min(pd)
    p = pn[pd.index(pd0)]
    hv[p[0]][p[1]] = 1
    if h[p[0]][p[1]] == 1: pe += [p]
    pn.remove(p)
    pd.remove(pd0)
#     print(p, pn, pd)
#     [print(e) for e in hd]
    if not pd:
        break
        

sc1 = hd[E[0]][E[1]]   # 447
sc2 = 446
print(f'part1: {sc1} \npart2: {sc2} ') # check that part is ok for HT[1]

# plotting
hd= [[e if e<hinf else 0 for e in row] for row in hd]
fig, axs = plt.subplots(3, 1, sharex=True) 
axs[0].imshow(h)
axs[1].imshow(hv)
axs[2].imshow(hd)
plt.show()
