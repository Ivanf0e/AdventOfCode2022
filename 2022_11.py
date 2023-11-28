import csv
import re
# 1. total changes of item value if every monkeys changes it and // 3, and throw to other monkey based on value, in sequence 
# rounds = 20

# 2. same but for 10000 rounds and no //3 (to do: this is now hard coded). so very high numbers.
# https://en.wikipedia.org/wiki/Modular_arithmetic
# if a % n == b % n, then for int k
# (a + k) % n == (b + k) % n
# (a * k) % n == (b * k) % n
# (a * k) % (k * n) == (b * k) % (k * n)
rounds = 10000

rounde = [1] + list(range(20,1000,20))+list(range(1000, rounds,1000))
it, itm, ops, opa, test, throw_true, throw_false = [], [], '', [], [], [], []

def fun(typ, e, a = 0):
    if   typ == '*': return e * a
    elif typ == '+': return e + a
    elif typ == 'o': return e * e

with open('2022_11_input.csv', 'r') as f:
    reader = csv.reader(f, delimiter=';')
    for k, row in enumerate(reader):
        c = k % 7
        if c == 1:
            its = [int(e) for e in re.findall(r'\d+', row[0])]
            it += its
            itm += [list(range(len(it)-len(its),len(it)))]
        elif c == 2:
            if row[0][19:] == 'old * old': ops += 'o'; opa += ['old']
            else: ops += row[0][23]; opa += [int(row[0][25:])];
        elif c == 3:
            test += [int(row[0][21:])]
        elif c == 4:
            throw_true += [int(row[0][29:])]
        elif c == 5:
            throw_false += [int(row[0][30:])]

itmod = [[e % t for t in test] for e in it]

ins = [0] * len(itm)
for j in range(rounds):
    for i, op in enumerate(ops):
        ins[i] += len(itm[i]) # total number of inspected elements
        while itm[i]: # while + pop, since monkey always throw always away
            e = itm[i].pop(0) # current item number
#             it[e] = fun(op, it[e], opa[i]) # // 3 #for part 1
#             throw2 = throw_false[i] if it[e] % test[i] else throw_true[i] # monkey to throw to
            itmod[e] = [fun(op, itmod[e][k], opa[i]) % t for k,t in enumerate(test)]
            throw2 = throw_false[i] if itmod[e][i] else throw_true[i] # monkey to throw to
#             if it[e] % test[i] !=  itmod[e][i]:
#             if throw2 == throw_true[i]:
#                 pass
            itm[throw2] += [e] # actually throw to this monkey

#     if j+1 in rounde: print(j+1, ins, itmod)
#     print([[it[e] for e in mon] for mon in itm])
ins_sort = sorted(ins)
sc = ins_sort[-2] * ins_sort[-1] # 117640 # 30616425600
print(f'solution: {sc}')