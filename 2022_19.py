import re, itertools
# https://github.com/jonathanpaulson/AdventOfCode/blob/master/2022/19.py
# https://topaz.github.io/paste/#XQAAAQDkBAAAAAAAAAA0m0pnuFI8c/T1npou3Ns2y6cWc/1crsV/u1SklIvndiVj4eISQO2llrtG+JGq5JGZ3XTHEWPvEXyMucXu4HHQs64Gv/M69eHG7hvueIBwcwFVgEy7D69leB6UT5FOnaOV/9W8UyNJZ/cv5E8oYR5uZI2QQU+wDiUILEghL6N5WrqVpAA9ru9Ow1Dd5LiSeD9gQo5aBWofsAPlyLdcFsX6PHLZT/TlR2l8I9jEahGp+u1NaeSTEBVI7FFZi9ZwgxzDYVRl2vmbCXlGPh+91r6i9Zo0forJt25x9TNOspOnBtIANCQGni/cmKKAorvCa+pUMpQ5W/zbc/4XH2BoY3tKS1IfSc1D5LpgS4GuXT3yM7EtAQ8w4B/0OaUOVtg9LJ106rGNsYc+N2UP8eDW0lO4gt5GZnRx7zEkxv7D5ObxQiucppVJq3QCMVa30xpmavpNq1z3Iclsqg+N64nRTgQvP5vG82LPu+rjRqP5vK5vQCE7Ng0caRWtlXcyBTrtkqQa/knT2nZihlrPxyjgjOB4T5qhLOeS8G6tM+emNjaxmdtdoKmFGOD7ii/EoVHp12dllMaiqMMLy/xKPiwnM0fQHVzPooni3FEbyGogsp3eJchIMB0jm+iYDf3DE8BnRWBngCMBMxw9lOxcbot2t0CuCZY89vsyB2g+bU49BhZz65MtCKU4QKMunYhp/cao1G+JgP68dFpfz32bkpcuAL83TNI5YYNL4rqbkJ6nw2nxAp5xw12NZZunKXPXjMLM8Afvb42j1bSAsn5G5WpY9nE5QaK6IBactySZWI7LidErrJ8LpVfvUVo4tv/xxELo
bps = [[int(u) for u in re.findall(r'\d+',l)] for l in open('2022_19.txt').read().splitlines()]
t2 = 8

S = (0,0,0,0,1,0,0,0,0) # state is ore, cly, obs, geo, Rore, Rcly, Robs, Rgeo, time)
def read_bp(bp):
    return [
        (-bp[1],0,0,0,1,0,0,0,0),
        (-bp[2],0,0,0,0,1,0,0,0),
        (-bp[3],-bp[4],0,0,0,0,1,0,0),
        (-bp[5],0,-bp[6],0,0,0,0,1,0)]
    

def ngbrs(S, bp, bpc):
    if S[8] == t1 or S[4] > bp[7] or S[5] > bp[4] or S[6] > bp[6] or max_geo(S) <= m: return {} # stop if time's up, more robots than cost, 
    N = tuple(sum(s) for s in zip(S,S[4:8] + (0,)*4 + (1,))) # new basic state
    return {N} | {tuple(sum(u) for u in zip(N, o)) for o in itertools.compress(bpc,
    [S[0] >= bp[1], # we are not building a robot if we saved up more material than needed
     S[0] >= bp[2],
     S[0] >= bp[3] and S[1] >= bp[4],
     S[0] >= bp[5] and S[2] >= bp[6]])}
    
def max_geo(S):
    return S[3] + S[7] * (t1 - S[8]) + (t1 - S[8] - 1) * (t1 - S[8])//2

# def max_ore(S):
    

r=1 # 0 for part 1, 1 for part 2
t1 = 32

for bp in bps[0:3]: # all for part 1, [0:3] for part 2
    bp.append(max(bp[1], bp[2], bp[3], bp[5])); bpc = read_bp(bp)



    m = 0 # max geodes possible at time t
    visited = set() # List for visited nodes.
    def dfs(visited, vertex):
        global m
        if vertex not in visited:
    #         print (vertex)
            visited.add(vertex)
            m = max(m, vertex[3]) 
            for ngbr in ngbrs(vertex, bp, bpc):
                dfs(visited, ngbr)

    dfs(visited, S)
    r *= m # += m * bp[0] for part 1, *= m for part 2
    print(m, len(visited))
# [print(v) for v in visited]
print(r) #960, 2040