# BFS using sets. Sets are so fast to look things up!
w, B, q, t = set(), set(), set(), 0 # locations for wall, blizzard and search directions in BFS. Hence time t is global

for y, line in enumerate(open("2022_24.txt")):
    for x, c in enumerate(line):
        if c=='#': w.add((x-1, y-1))
        if c=='>': B.add((x-1, y-1, +1, 0)) #x, y, dx, dy
        if c=='<': B.add((x-1, y-1, -1, 0))
        if c=='^': B.add((x-1, y-1, 0, -1))
        if c=='v': B.add((x-1, y-1, 0, +1))

xu, yu = max(x for x,y in w), max(y for x,y in w)
w |= {(0,-2), (xu-1,yu+1)} #(x,-2) for x in range(-1,2)}
# w |= {(x,yu+1) for x in range(xu-2,xu)}

q.add((0,-1))
g = [(xu-1,yu), (0,-1), (xu-1,yu)]

while g:
    t += 1
    b = {((x + dx*t)%xu, (y + dy*t)%yu) for x,y,dx,dy in B} # blizards move only in one directions
    s = {(x+dx, y+dy) for dx,dy in ((+1,0), (0,+1), (-1,0), (0,-1), (0,0)) for x,y in q}
    q = s - b - w
    if g[0] in q:
        print(t)
        q = {g.pop(0)}



# def move(b,d):
#     if d == '>': return (1 if b[0] == xu else b[0] + 1, b[1])
#     if d == '<': return (xu if b[0] == 1 else b[0] - 1, b[1])
#     if d == 'v': return (b[0], 1 if b[1] == yu else b[1] + 1)
#     if d == '^': return (b[0], yu if b[1] == 1 else b[1] - 1)
# 
# 
# 
# def plot():
#     plt = []
#     for y in range(yl,yu+1):
#         plt.append(['.' for x in range(xl,xu+1)])
#     plt[S[1]-yl][S[0]-xl] = 'E'
#     for b,d in zip(blzl, blzd):
#         plt[b[1]-yl][b[0]-xl] = d
#     for l in plt:
#         print(''.join(l))
#     print()
# 
# 
# 
# def ngbrs(S, visited):
#     global m
#     s, t0, N = S[0:2], S[2]+1, set(); t, bs = (t0,), blzsl[t0 % blz_rep]
#     if t0 >= m: return {}
#     if (t1 := t0 - blz_rep) > 0 and (s+(t1,)) in visited:
#         print(S)
#         return N # remove if staying tool long]
#     if s == (xu,yu): m = min(m, t0); print(m); return {}
#     if s[1] < yu and not (n:= (s[0],s[1]+1)) in bs: N.add(n+t) 
#     if s == (1,0): return N if N else {(s+t)}
#     if s[0] < xu and not (n:= (s[0]+1,s[1])) in bs: N.add(n+t) # to do import operator as op
#     if s[0] > xl and not (n:= (s[0]-1,s[1])) in bs: N.add(n+t) # then try something like:
#     if s[1] > yl and not (n:= (s[0],s[1]-1)) in bs: N.add(n+t) # oplist =  [[1, op.ge], [0, op.ge], [1, op.lt], [0, op.lt]]
#     if not s in bs: N.add(s+t)
# #     print(N)
#     return N


# blzd, blzl = tuple(b[2] for b in blzl), [tuple(b[0:2]) for b in blzl]
# xl,xu = min(r:=[v[0] for v in blzl]), max(r)
# yl,yu = min(r:=[v[1] for v in blzl]), max(r)

# blz_rep = 0 # cycles before system repeats. needed for DFS as cycle may repaat itself
# while (blz_rep := xu + blz_rep) % yu: pass
# blzsl = [set(blzl)]
# for i in range(blz_rep):
#     blzl = [move(b,d) for b,d in zip(blzl, blzd)] # update blz positions
#     blzsl.append(set(blzl))


# S = (1,0,0) # state is position and time

# m = 100000 # some max score  # DBS was too slow and ran into recursive max error
# visited = set() # List for visited nodes.
# def dfs(visited, vertex):
#     global m
#     if vertex not in visited:
#         visited.add(vertex)
# #         print(visited)
# #         m = max(m, vertex[3]) 
#         for ngbr in ngbrs(vertex, visited):
#             dfs(visited, ngbr)
# #         print(m, len(visited))
# dfs(visited, S)
# print(m, len(visited))

# ans_ex = [(1,1,1),(1,2,2),(1,2,3),(1,1,4),(2,1,5),(3,1,6),(3,2,7),(2,2,8),(2,1,9),(3,1,10),(3,1,11),(3,2,12),(3,3,13),(4,3,14),(5,3,15),(6,3,16),(6,4,17)]
# [l in visited for l in ans_ex]
# [r in ngbrs(s, visited) for s,r in zip(ans_ex, ans_ex[1:])]