import csv
# A, X for Rock, 1
# B, Y for Paper, 2
# C, Z for Scissors, 3
with open('2022_2_input.csv', 'r') as f:
    reader = csv.reader(f)
    sc1, sc2 = 0, 0
    dict1 = {
        "A;X": 4,
        "A;Y": 8,
        "A;Z": 3,
        "B;X": 1,
        "B;Y": 5,
        "B;Z": 9,
        "C;X": 7,
        "C;Y": 2,
        "C;Z": 6,}
    
    dict2 = {
        "A;X": 3,
        "A;Y": 4,
        "A;Z": 8,
        "B;X": 1,
        "B;Y": 5,
        "B;Z": 9,
        "C;X": 2,
        "C;Y": 6,
        "C;Z": 7,}

    for i, row in enumerate(reader):
        sc1 += dict1[row[0]]        
        sc2 += dict2[row[0]]
        #print(row, dict2[row[0]])
        #if i == 4: break

print(f'part1: {sc1} points')
print(f'part2: {sc2} points')