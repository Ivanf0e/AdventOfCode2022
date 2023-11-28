import re, itertools
for dk, ln in [(1, 1), (811589153, 10)]:
    seq = [int(l)*dk for l in open('2022_20.txt').read().splitlines()] # 17490, 1632917375836
#     seq = [v*dk for v in [1,2,-3,3,-2,0,4]]      # example code 3, 1623178306

    n = len(seq); nn = n - 1; o = list(range(n)) # make list to track indices
    s = [v for v in seq]                         # deep copy of original list

    for l in range(ln):                          # do mixing this many times
        for j in range(n):                       # for entire sequence
            i = o.index(j); o.pop(i)             # numbers should be moved in the order they originally appear
            v = s.pop(i)                         # get the actual number out of new sequence
            k = (i + v + nn) % nn                # here it should be inserted in
            o.insert(k, j); s.insert(k, v)       # do actual inserting
    #         print(list(zip(o[0:10],s[0:10])))
#     print(i,v, k, (i + v + nn) % nn, p0:=s.index(0)) 
    print(sum([s[(s.index(0) + w)%n] for w in [1000,2000,3000]]))