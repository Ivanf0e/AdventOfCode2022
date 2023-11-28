# 1 heigth of tower of falling rocks
w, x0, y0, y1 = 7, 2, 3, 4 # width of chamber, and start horizontal offset of rock

# wind = '>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>'; # example input
wind = open('2022_17.txt').read()
windi = -1; windn = len(wind)

rockkind = [ # x, y, other elements of falling rock
    [x0, 0, 1, 2, [[0,0], [1,0],[2,0],[3,0]]], # -
    [x0, 0, 3, 3, [[1,0], [0,1],[1,1],[2,1],[1,2]]], # +
    [x0, 0, 3, 3, [[0,0], [1,0],[2,0],[2,1],[2,2]]], # _|
    [x0, 0, 4, 5, [[0,0], [0,1],[0,2],[0,3]]], # |
    [x0, 0, 2, 4, [[0,0], [0,1],[1,0],[1,1]]]] # [] 

twr = [list(range(w))] # tower of stationary rock at [y][x], so we only need to check relevant row
twrh, twro = len(twr), 0 # heigth and offset of tower. only start searching here
rep, repv, twrht = [], [], [] # keep track of tower until process repeats itself


def collison():
    for [x,y] in rockkind[kind][4]:
        if rock[1]+y < twrh: # rock in range of twr
            if rock[0] + x in twr[rock[1]+y-twro]:
                return True
    return False

def etrp(tn):
    if tn< len(twrht): return twrht[tn] -1
    tr=((tn-d)//c)*c+d
    return int((a*tr+b)/c + twrht[d+t1-tr]-twrht[d]-1)

for t in range(100000):
    while len(twr) > 100:
        twr.pop(0)
        twro += 1
    kind = t % 5 # to do: track if we can find a repetition
    rock = rockkind[kind][0:2]
    rock[1] += twrh + y0
#     print(rock, kind)
    twrht.append(twrh)
    if kind == 0:
        if windi in rep:
            tp, twrhp = repv[rep.index(windi)]
            a, c = twrh - twrhp, t - tp
            b, d = twrhp*c - tp * a, t - c
#             print(t, windi, twrh, tp, twrhp, a, b, c, d)
            break
        else: rep.append(windi); repv.append((t,twrh))
    while True: #for j in range(y1):
        windi = (windi + 1) % windn
        if wind[windi] == '>' and rock[0] <= rockkind[kind][3]:
            rock[0] += 1
            if collison(): rock[0] -= 1
        elif wind[windi] == '<' and rock[0] >= 1: # no 
            rock[0] -= 1
            if collison(): rock[0] += 1
        rock[1] -= 1 # drop 1
        if collison():
            rock[1] += 1
            dy = rock[1] - twrh + rockkind[kind][2]
            if dy>0:
                twr += [[] for _ in range(dy)]
                twrh += dy
            for [x,y] in rockkind[kind][4]:
                twr[rock[1]+y-twro] += [rock[0] + x]
            break
#         print(rock)    
# [print(''.join(['#' if u in v else '.' for u in range(w)])) for v in twr[::-1]]

# tr=((t1-d)//c)*c+d
# print((a*tr+b)/c + twrht[d+t1-tr]-twrht[d]-1)
print(etrp(2022), etrp(1000000000000))