import math

def snafu(e):
    d,b=0,1
    for c in e[::-1]:
        if c =='-': c = -1
        elif c == '=': c = -2
        else: c = int(c)
        d += b * c
        b *= 5
    return(d)

D = []
for i, line in enumerate(open("2022_25.txt").read().splitlines()):
    D.append(snafu(line))



d,e  = sum(D), ''; r = d
b = int(math.log(d)/math.log(5) // 1.0)
c2e = ['=','-','0','1','2']
while b>-1:
    c = (l:=[abs(r/5**(b-1) - i*5) for i in range(-2,3)]).index(min(l))
    e += c2e[c]
    r -= (c-2) * 5**b
    b -= 1
#     print(l,c,r)

print(d, e)
print(snafu(e))