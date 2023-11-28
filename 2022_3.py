import csv
import string
# 1. find same letter (case sensitive) 1st and 2nd half of row
# Lowercase item types a through z have priorities 1 through 26.
# Uppercase item types A through Z have priorities 27 through 52.


prio_dict = dict(zip(list(string.ascii_lowercase + string.ascii_uppercase),
        list(range(1,53))))
with open('2022_3_input.csv', 'r') as f:
    reader = csv.reader(f)
    sc1, sc2 = 0, 0
    gr = [0]*2

    for i, row in enumerate(reader):
        r = row[0]
        n = int(len(r) / 2)
        dub = [e for e in r[0:n] if e in r[n:]]
#         print(dub)
        # sc1 += sum([prio_dict[e] for e in dub]) # apprently not correct if more then one instance
        sc1 += sum([prio_dict[e] for e in set(dub)])
        
        
        if i % 3 == 2:
            dub = [e for e in r if e in gr[0] and e in gr[1]]
            sc2 += sum([prio_dict[e] for e in set(dub)])
        else:
            gr[i % 3] = r
#         if i == 3: break


print(f'part1: {sc1} points')
print(f'part2: {sc2} points')