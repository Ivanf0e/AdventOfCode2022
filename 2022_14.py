# 1. units of sand at rest when sand originates at 500,0, and goes down, down-left or down-right, if not blocked by other sand or rock input
# 2. same with a floor at max(y) 2 at infinite x, and simulate until reaches sources
S =  [500, 0]
X, Y, D, sc1 = [S[0]], [S[1]], S, 0 #current drop location of sand
with open('2022_14_ex.csv', 'r') as f:
    import csv, re
    reader = csv.reader(f, delimiter=';')
    for k, r in enumerate(reader):
        if r:
            rr = [int(e) for e in re.findall(r'\d+', r[0])]
            x0,y0 = rr[0], rr[1]
            X += [x0]; Y+= [y0]
            for s in range(2, len(rr), 2):
                x1, y1 = rr[s], rr[s+1]
                X += [x1]; Y+= [y1]
                if x0 == x1: # x range does not change
                    for y in range(y0, y1, 1 if y0<=y1 else -1): X += [x0]; Y+= [y]
                else:
                    for x in range(x0, x1, 1 if x0<=x1 else -1): X += [x]; Y+= [y0]    
#                 print(X,Y)
                x0, y0 = x1, y1

# part 2 (comment out for part 1)
# y0 = max(Y) + 2
# x0, x1 = S[0] - y0 - 1, S[0] + y0 + 2
# for x in range(x0, x1, 1 if x0<=x1 else -1): X += [x]; Y+= [y0]

ranges = [min(X), max(X), min(Y), max(Y)]
row, col = ranges[3] - ranges[2] +1 , ranges[1] - ranges[0] + 1
h  = [[0 for i in range(col)] for j in range(row)]

def hset(xy, val=2):
    h[xy[1] - ranges[2]][xy[0] - ranges[0]] = val

def hget(xy, offset=[0,0]):
    return h[xy[1] - ranges[2] + offset[1]][xy[0] - ranges[0] + offset[0]]
    
def hlrm(xy):
    retrhget(xy), hget(xy, [-1,1])

for xy in zip(X,Y):
    hset(xy, 1)
hset(D,0)


# D[1] =
E = [D[0], next(i for i,v in enumerate([r[D[0]-ranges[0]] for r in h]) if v) + ranges[2]] # moving sand location

for j in range(10000000): # cap iterations
    if hget(E): # obstruction at location, try to fall left
        if hget(E,[-1,0]): # something on left
            if hget(E,[1,0]): # something on right
                E[1] -= 1
                hset(E) # sand becomes stationary
                sc1 += 1
                E = [D[0], next(i for i,v in enumerate([r[D[0]-ranges[0]] for r in h]) if v) + ranges[2]] # moving sand location
                if E == D: break
            else: # nothing on right
                E[0] += 1
                if E[0] > ranges[1]: break
        else: # nothing on left
            E[0] -= 1
            if E[0] < ranges[0]: break
    else: # no obstruction keep falling
        E[1] += 1
        if E[1] > ranges[3]: break # fall into void
#     if E == [489, 10]:
#         print(E)

hset(D,.5) # give other value to start pos

print(f'sand parts: {sc1}') # check that part is ok for HT[1]

# plotting
import matplotlib.pyplot as plt
# with plt.ion(): # chrashes every time
fig, axs = plt.subplots(1, 1, sharex=True) 
axs.imshow(h, extent=ranges[0:2]+ranges[-1:-3:-1])
# axs[1].imshow(hv)
# axs[2].imshow(hd)
plt.show()
