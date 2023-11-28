# 1. in row y1, locations where no beacons can be, which is in taxicab distance from sensor to nearest beacon
y1 = 10 # 2000000 # 
# 2. single possible beacon in range square. ans = x * ranges[1] + y
# take to long to loop over entire grid. to do : look at edge of circle

ranges = [0,4000000] #[0, 20] #
with open('2022_15ex.txt') as file:
    import re
    locr = [[int(b[i]) for i in (1,3,5,7)] for b in \
        [re.split('=|,|:', c) for c in file.read().splitlines()]]
beac =  set()# only unique elements where a beacon cannot be


def unionranges(a):
    # https://stackoverflow.com/questions/15273693/union-of-multiple-ranges
    b = []
    for begin,end in sorted(a):
        if b and b[-1][1] >= begin - 1:
            b[-1][1] = max(b[-1][1], end)
        else:
            b.append([begin, end])
    return b

for y1 in range(ranges[1]): # y1 = 10  # 10 for step 1
    occuy1, occuL, occuR, LRrange  = [] , y1, -y1, []

    for loc in locs:
        loc += [d := abs(loc[0] - loc[2]) + abs(loc[1] - loc[3])]
        if loc[1] == y1: beac.add((loc[0], loc[1]))
        if loc[3] == y1: beac.add((loc[2], loc[3]))
        
        if (dy := y1 - loc[1]) >= -d and dy <= d:
            L, R = loc[0] - d + abs(dy), loc[0] + d - abs(dy) # assume overlapping
            occuL, occuR = min(L, occuL), max(R, occuR)
            LRrange += [(L, R)]
            occuy1 += [[L, R, loc[0:2], d]]
    if len(b:= unionranges(LRrange)) > 1:
        print(b, y1)
        x1 = b[0][1]+1 # 3405562, 3246513
        break
#     print(occuy1)
#     sc1 = occuR - occuL +1 - len(beac) # 4724228

sc1 = 4724228
print(f'no beacon: {sc1}. tuning frequency: {x1 * 4000000 + y1}') # check that part is ok for HT[1]

# plotting
# import matplotlib.pyplot as plt
# # with plt.ion(): # chrashes every time
# ranges = (min(x:=[s[0] for s in occu]), max(x)+1, min(y:=[s[1] for s in occu]), max(y)+1)
# h = [[0 for _ in range(ranges[1] - ranges[0] +1)] for _ in range(ranges[3] - ranges[2] +1)]
# def hset(xy, val=2):
#     h[xy[1] - ranges[2]][xy[0] - ranges[0]] = val
# for s in occu: hset(s,1)
# for loc in locs:
#     hset(loc[0:2], 2)
#     hset(loc[2:4], 3)
# fig, axs = plt.subplots(1, 1, sharex=True) 
# axs.imshow(h, extent=ranges[0:2]+ranges[-1:-3:-1])
# # axs[1].imshow(hv)
# # axs[2].imshow(hd)
# plt.show()