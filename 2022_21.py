from collections import defaultdict
import copy

d = defaultdict(lambda: [None, [], None, None, None, None, None])
# default dict for value, yelled to, waiting for others (2), operation, values of others (2)

for l in open('2022_21.txt').read().splitlines():
    k,v = l[0:4], l[6:]
    if v.isdigit(): d[k][0] = int(v) # update yelled value
    else:                            # update monkeys to wait for
        d[k][2:5] = (mw:=[v[0:4], v[7:11]]) + [v[5]]
        [d[kb][1].append(k) for kb in mw]

def updt(k,ver=False):
    for kb in d[k][1]:
        if ver: ops.append([kb]+ d[kb][4:7] +[k]) # add to the function list
#             print(kb, d[kb][4:7],k)
        d[kb][d[kb].index(k)+3] = d[k][0]
        if not any([a is None for a in d[kb][5:7]]):
            p,q,r = d[kb][4:7]
            if   p == '+': d[kb][0] = q + r
            elif p == '-': d[kb][0] = q - r
            elif p == '*': d[kb][0] = q * r
            elif p == '/': d[kb][0] = q // r
            updt(kb,ver)

x,  d['humn'][0] = d['humn'][0], None # for part 2 'humn' is input so temporary remove
[updt(k) for k,v in d.items() if v[0]] # do monkey shouts as if 'humn' was not there
dels = [k for k,v in d.items() if v[0]] # all values that are available without 'humn'
[d.pop(k) for k in dels] # delete the ones that do not depent on 'humn'
db = copy.deepcopy(d)
ops = [] # list of operators

d['humn'][0] = x   # do monkey shouts with 'humn' on limited set for part 1
updt('humn', True)
print(d['root'][0]) # part 1: 21120928600114

y = ops[-1][2] if ops[-1][2] else ops[-1][3]; s=str(y) # value needed for part 2 by 'root'
k_check = ops[-1][-1]           # s= (3+((4*150)-4)//2) # this should be formula for example
for op in ops[len(ops)-2::-1]:  # reconstruct the formula starting from root. only works for 1 unknown per monkey
    if op[0] != k_check: print('unexpected value')
    p = op[1] # calculate with this value
    l = bool(op[2]) # left or right of op
    q = str(op[2]) if l else str(op[3])
    if p =='+': s = '('+s+'-'+q+')'
    elif p =='-':
        if l: s = '('+q+'-'+s+')'
        else: s = '('+s+'+'+q+')'
    elif p =='*': s = '('+s+'//'+q+')'
    elif p =='/':
        if l: s = '('+q+'//'+s+')'
        else: s = '('+s+'*'+q+')'
    if not any([a is None for a in ops[0][2:4]]): print('wait for more monkeys?', op, s)
#     print(s)
    k_check = op[-1]
print(eval(s)) # 3453748220116

d = copy.deepcopy(db)     # check if correct
d['humn'][0] = eval(s)
updt('humn')
if d['root'][5] != d['root'][6]: print('something went wrong')