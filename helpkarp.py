# https://en.wikipedia.org/wiki/Held%E2%80%93Karp_algorithm
from itertools import combinations
def tplm(tpl, v):
    return tuple(e for e in tpl if e != v)

def helpkarp(d):
    n = len(d)
    r = list(range(n))
    g, p = {}, {}
    g.update({'()': [d[k][0] for k in range(n)]})
    p.update({'()': [0 for k in range(n)]}) # zeroth item always points back to zero

    for s in range(1, n-1):
        for S in combinations(range(1, n), s):
            g.update({str(S) : [0]*n})
            p.update({str(S) : [None]*n})
            for k in range(1, n): # no need to evalute zeroth
                if k not in S:
                    g[str(S)][k] = min(b := [d[k][a] + g[str(tplm(S,a))][a] for a in S]) #d[k][S[0]] + g['()'][S[0]]
                    p[str(S)][k] = S[b.index(g[str(S)][k])]
#                     print(b, S, S[b.index(g[str(S)][k])])
#                     for a in S:
#                         print(S, a, k, tplm(S,a), d[k][a], g[str(tplm(S,a))][a])
#                     print(min([d[k][a] + g[str(tplm(S,a))][a] for a in S]))
#                     [print(v[0], v[1]) for v in g.items()]
    for S in combinations(range(1, n), s+1): # should be one item, ie all items except 0
        k = 0  # only need to evaluate zeroth
        g.update({str(S) : min(b := [d[k][a] + g[str(tplm(S,a))][a] for a in S])})
        p.update({str(S) : S[b.index(g[str(S)])]})

#     [print(v[0], v[1]) for v in g.items()]
#     [print(v[0], v[1]) for v in p.items()]
    
    length, path = g[str(S)], [p[str(S)], 0]
    while S:
        S = tplm(S,path[0])
#         print(S, path, p[str(S)][path[0]])
        path.insert(0,p[str(S)][path[0]])
    return length, path

if __name__ == "__main__":
    nodes = ('A', 'B', 'C', 'D')
    distances = [
        [0,2,9,10],
        [1,0,6,4],
        [15,7,0,8],
        [6,3,12,0]] # (21, [0, 1, 3, 2, 0])
     
    d=[[0,6,1,3],
       [6,0,4,3],
       [1,4,0,2],
       [3,3,2,0]] # (11, [0, 3, 1, 2, 0])
    
    d1 =  [[0 ,49, 34, 96, 74],
    [49,  0 ,10, 94 ,43],
    [34 ,10 , 0 ,21 , 6],
    [96, 94 ,21 , 0 ,70],
    [74, 43,  6 ,70,  0]] # (215, [0, 3, 2, 4, 1, 0])
    
    d2 = [[ 0,  2,  9, 10],
    [ 1,  0,  6 , 4],
    [15,  7,  0 , 8],
     [6 , 3, 12 , 0]]
    print(helpkarp(d)) # (21, [0, 1, 3, 2, 0])