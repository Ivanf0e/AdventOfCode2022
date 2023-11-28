from itertools import zip_longest
# 1. sum of index of packets pairs for correct rules
# 2. prod of indices of p2, p6 in sorted list.
# we can use the code now developed to check how often p2,p6 are for correct rules
p2, p6 = [[2]], [[6]]
sp = '  '
def lstcom(p0, p1, it): # returns bools for stop, rules
    pl = [type(p0) is list, type(p1) is list]
#     print(f'{sp*it} {p0} <> {p1}')
    if all(pl): # rule 2        
        pass
    elif any(pl): # rule 3: make integer in a list
        if pl[1]: p0 = [p0]
        else: p1 = [p1]
    else: # rule 1: first should be smaller then right
        return (p0 == p1, p0 <= p1)
    go = True # in case empty list

    for ii, p in enumerate(zip(p0, p1)):
        go, ok = lstcom(p[0], p[1], it+1) # it to keep track of it number
        if not go: break
            
    if not(p0): # if both are [] we still continue
        go, ok = not(p1), True
    elif len(p0) < len(p1) and go: # left side ran out of items
        go = False
    elif len(p0) > len(p1) and go: # right side ran out of items
        go = ok = False
    
    return (go, ok)

newpair, porder, p2order, p6order = False, [], [], []
# with open('2022_13_ex.csv', 'r') as f:
with open('2022_13_input.csv', 'r') as f:
    import csv
    reader = csv.reader(f, delimiter=';')
    for k, row in enumerate(reader):
        if row:
            p1 = eval(row[0])
            p2order += [lstcom(p1, p2, 0)[1]]
            if p2order[-1]: p6order += [True] # safe a little time since p6 always above p2
            else:
                p6order += [lstcom(p1, p6, 0)[1]]
#             print(p2order[-1], p6order[-1])
            if newpair:
#                 print(f'== Pair {len(porder)+1} ==')
                porder += [lstcom(p0, p1, 0)[1]]
#                 print(porder[-1])
                pass

                newpair = False
            else:
                newpair = True
                p0 = p1
  
pi2 = 1 + sum([1 for i,pb in enumerate(p2order) if pb])
pi6 = 2 + sum([1 for i,pb in enumerate(p6order) if pb])

sc1 = sum([i+1 for i,pb in enumerate(porder) if pb]) # 5625
sc2 = pi2 * pi6 # 23111
print(f'part1: {sc1} \npart2: {sc2} ')
