import itertools

# with open("2022_18ex.txt") as f:
#     cubes = [tuple(map(int, re.findall("(\d+)", l))) for l in f.readlines()]
cubes = {tuple(map(int,l.split(','))) for l in open('2022_18.txt')}
minout = [min(c[i]-1 for c in cubes) for i in range(3)]
maxout = [max(c[i]+1 for c in cubes) for i in range(3)]


def in_space(cube):
    return all(minout[i] <= cube[i] <= maxout[i] for i in range(3))


def get_neighbors(cube):
    return [tuple(sum(x) for x in zip(cube, d)) for d in [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]]

# part 1
exposed = sum([(s not in cubes) for c in cubes for s in get_neighbors(c)])

# part 2
exposed_outside = 0
seen = set()
queue = [tuple(maxout)]
while queue:
    curr_cube = queue.pop(0)
    if curr_cube in cubes:
        exposed_outside += 1
        continue
    if curr_cube not in seen:
        seen.add(curr_cube)
        for n in get_neighbors(curr_cube):
            if in_space(n):
                queue.append(n)

print(exposed)
print(exposed_outside)


world = set()
minw = [min(c[i] for c in seen) for i in range(3)]
maxw = [max(c[i]+1 for c in seen) for i in range(3)]
for x,y,z in itertools.product(range(minw[0], maxw[0]),range(minw[1], maxw[1]),range(minw[2], maxw[2])):
    world.add((x,y,z))        

voids = world - seen - cubes

import matplotlib.pyplot as plt
ax = plt.figure().add_subplot(projection='3d')
# x,y,z = [[c[i] for c  in cubes] for i in range(3)]
# ax.scatter(x,y,z)
xv,yv,zv = [[c[i] for c  in voids] for i in range(3)]
ax.scatter(xv,yv,zv)
ax.set_xlabel('X');ax.set_ylabel('Y');ax.set_zlabel('Z')
plt.show()