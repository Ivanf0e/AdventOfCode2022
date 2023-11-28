import csv
import re
# 1. sum of directories, which size <
s1 = 100000
# 2. smallest directory to make available, for total system of
s20, s21 = 30000000,70000000

tot = 0
main = '/'
dir_names = [main] # name of all dir_names
dir_size = [0]
dir_par = [-1]

with open('2022_7_input.csv', 'r') as f:
    reader = csv.reader(f)
    
    for i, row in enumerate(reader):
        r = row[0]
        if r[:4] == '$ cd': # change directory cmd
            if r[5:] == main:
                dirc, dirn = main, 0 # current directory number and inex
            elif r[5:] == '..': # go up one higher
                dirc = dir_names[dir_par[dirn]]
            else: # step into
                dirc += [r[5:]][0] + main
                if not dirc in dir_names: # new directory
                    dir_par += [dirn]
                    dir_names += [dirc]
                    dir_size += [0]
            dirn = dir_names.index(dirc)
        elif r[:4] == '$ ls':
            pass # starting listing
        elif r[:3] =='dir':
            pass # directory in this folder
        else:
            fsize = int(re.findall(r'\d+', r)[0])
            j = dirn
            while not j == -1:
                dir_size[j] += fsize
                j = dir_par[j]
            tot += fsize
#             print(dirc, dir_par, dir_names, fsize, dir_size)
#         if i == 42: break
if dir_size[0] != tot: print('totals nok')
sc1 = sum([s for s in dir_size if s <=s1]) # 1348005
s2 = s20 - (s21 - tot)
sc2 = min([s for s in dir_size if s >=s2]) # 12785886

print(f'part1: {sc1} \npart2: {sc2} ')