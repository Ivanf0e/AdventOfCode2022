from collections import defaultdict
pc = [x+y*1j for y,r in enumerate(open('2022_23.txt').read().splitlines()) for x,c in enumerate(r) if c=='#'] # elf original positions
# pc = [0,1,1j,3j,1+3j];

nn = [1-1j,-1j, -1-1j, -1, -1+1j, 1j, 1+1j, 1] # neareast neighbours
sn = [-1j,1j,-1,1];                            # step if allowed, so N,S,W,E = 0,1,2,3
qn = [[0,1,2],[4,5,6],[2,3,4],[6,7,0]]         # search in these nn per step in sn

def prnt(pc):
    xl,xu = min(r:=[int(v.real) for v in pc]), max(r)
    yl,yu = min(r:=[int(v.imag) for v in pc]), max(r)
    e = (yu+1-yl) * (xu+1-xl) - len(pc)
#     for y in range(yl,yu+1):
#         r = [0 if x+y*1j in pc else 1 for x in range(xl,xu+1)]
#         e += sum(r)
#         print(''.join(['.' if v else '#' for v in r]))
    print(e)

def sug(pn): # suggest to move where
    for q,s in zip(qn,sn):
        if not any([pn[v] for v in q]):
            return s
    return 0

pnb, j = True, 0
while pnb:
    psug, pc_speed, pnb, j = defaultdict(list), set(pc), 0, j+1 # step suggestion, elves set (for spped) and duplicates
    
    for i, p in enumerate(pc):                     # keep track of elf id instead of finding duplicates and index during search
        if any(pn:=[p+n in pc_speed for n in nn]): # check all nn for elves
            psug[p+sug(pn)].append(i)

    for p, i in psug.items():                      # or change dict to a single index that will be false if we add another
        if len(i) == 1:
            pc[i[0]] = p
            pnb += 1

    sn = sn[1:]+sn[0:1]; qn = qn[1:]+qn[0:1]       # change search direction
    if j == 10:  prnt(pc)

print(j)