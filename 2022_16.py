# 1. max pressure released after t1,  when moving to or opening a vavle is 1 min, and flow rate [pressure/min] and possible paths given
t1, s0 = 30, 'AA' # min, start loc
# 2. single possible beacon in range square. ans = x * ranges[1] + y
# take to long to loop over entire grid. to do : look at edge of circle
from dijkstra import dijkstra
from helpkarp import helpkarp
import itertools

def release(order):
    t, P = t1, 0
    for s in zip([s0]+order,order): # always start at first valve
        print(L[s[1]][s[0]], F[s[1]])
        t -= L[s[1]][s[0]] + 1
        if t <= 0: break
        P += t * F[s[1]]
    return P

def swap1(order, i0, n):
    order[i0], order [i0+n] = order[i0+n], order [i0]

with open('2022_16.txt') as file:
    import re
    inpt = [[(d := re.split('=|;| has|valves |valve |Valve ', c)) \
          [1], int(d[3]), d[5].split(', ')] for c in file.read().splitlines()]
#     valve, flow, tunnel = [[row[i] for row  in inpt] for i in range(3)] #
#     d = {v[0]: i for i,v in enumerate(valve)} 
# start at AA !!!!!
n, D, L, F, Q, Qu = len(inpt), {}, {}, {}, [], 0
for v in inpt: #zip(valve, flow):(v, f, dirs) 
    D.update({v[0]:{a:1 for a in v[2]}})
    F.update({v[0]:v[1]})
for v in F.items():
    if v[1]:
        L.update({v[0]: dijkstra(F.keys(), D, v[0])})  #[[d[w] for w in valve]]})
[print(v[0], v[1]) for v in L.items()]

# brute force
# for p in itertools.permutations(L.keys()): # per is generator object:
#     Qu = max(Qu, release(list(p)))

# TSP, but how to include flows?
# print(helpkarp(dist:=[[L[w][v] for v in L.keys()] for w in L.keys()]))

# sort in 2 lists [[w[i] for w in [v for v in sorted((F.items()), key=lambda x:x[1], reverse=True)]] for i in [0,1]]
# sort in 1 list Fs = [v for v in sorted((F.items()), key=lambda x:x[1], reverse=True)]
p = [v[0] for v in sorted((F.items()), key=lambda x:x[1], reverse = True) if v[1]]

r = release(p)
for j in range(4):
    for i in range(len(p)): 
        swap1(p, i, 1)
        print(rn:=release(p), p)
        if r > rn:
            swap1(p, i+1, -1)
            print(i)
            break
        else:
            r = rn        
    if i ==0: break
# 1720 2582
# p = ('DD', 'BB', 'JJ', 'HH', 'EE', 'CC') # correct answer


# presmax = sum([a*flow[b] for a,b in zip(range(t1-2, t1-2-2*len(flows),-2), flowi)])
# tree, valve_on, presl, presu = [[0]], [[]], [0], [presmax]
# 
# 
# # kk = [0,0,2,5,9,8,8,14,15,17,17,18,18,19,23,24,26,27,27,28,28,29,30,33,33]
# # for t in range(len(kk)):
# #     k = kk.pop(0)
# for t in range(10):
#     presa = [a+b for a,b in zip(presl,presu)]
#     k = presa.index(max(presa)) # pick this branch, since most potential
#     br = tree.pop(k)
#     tm = t1 - len(br) # time left in branch
#     vo = valve_on.pop(k)
#     pu = presu.pop(k)
#     pl = presl.pop(k)
#     
# #     for j in range(i0, i1:=len(tree)):
#     
#     if not (f:=br[-1]) in vo and flow[f]: # f is current node
#         tree += [br + [f]]
#         valve_on += [vo + [f]]
#         presl += [pl + flow[f] * tm]
#         flowpi = [v for v in flowi if not v in valve_on[-1]] # index of flows that are unvisited
#         if flowpi:
#             presu += [presl[-1] + sum([a*flow[b] for a,b in zip(range(tm-1, tm-1-2*len(flowpi),-2), flowpi)])]
#         else: #stop branch because all valves open
#             if presl[-1] != pu: print(pl, presl[-1], flow[f], 'error in convergence')
#             presu += [presl[-1]]
#             presl[-1] = 0 #'stop'
#     for fn in inpt[f][2]: # fn are new nodes
#         tree += [br + [fn] ]
#         valve_on += [vo]
#         presl += [pl]
#         flowpi = [v for v in flowi if not v in valve_on[-1]] # index of flows that are unvisited
#         presu += [presl[-1] + sum([a*flow[b] for a,b in zip(range(tm-1, tm-1-2*len(flowpi),-2), flowpi)])]
#     
# [print(b) for b in zip(presl, presu, valve_on, tree)]
# print(len(tree)-1)


sc1 = 4724228
print(f'pressure released: {r}. part 2: {0}') # check that part is ok for HT[1]