import collections as c, itertools, functools, re

r = r'Valve (\w+) .*=(\d*); .* valves? (.*)'

V, F, D = set(), dict(), c.defaultdict(lambda: 1000) # if not exsistent entry, dd makes new one with function

for v, f, us in re.findall(r, open('2022_16.txt').read()):
    V.add(v)                                  # store node
    if f != '0': F[v] = int(f)                # store flow
    for u in us.split(', '): D[u,v] = 1       # store dist, similar to sparse matrix

for k, i, j in itertools.product(V, V, V):    # nested for loop. by letting k increase, we are looking at alls k-1 LHS
    D[i,j] = min(D[i,j], D[i,k] + D[k,j])     # floyd-warshall

@functools.cache
def search(t, u='AA', vs=frozenset(F), e=False): # vs are all non-discovered vertices
    # for all possible directed edges from u to v
    # label v as dicovered if not discovered (ie subtract from undiscovered set)
    # recursively do for v
    w = [F[v] * (t-D[u,v]-1) + search(t-D[u,v]-1, v, vs-{v}, e) 
           for v in vs if D[u,v]<t] + [search(26, vs=vs) if e else 0] # do as if the 2nd player starts after you and can only open valves (non-discovered vortices)
#     print(w)
    return max(w)

print(search(30), search(26, e=True))