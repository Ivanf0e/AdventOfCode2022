def neighbors(cube):
    return {tuple(u+w for u,w in zip(cube, o)) for o in [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]}

cubes = {tuple(map(int,l.split(','))) for l in open('2022_18.txt')} # 4348

print(sum([(s not in cubes) for c in cubes for s in neighbors(c)]))
# interior can be quite large, ie nearest neighbors are not sufficient.
# hence BFS starting outside. although need to limit search area:
cl, cu = min([min(c[i] for c in cubes) for i in range(3)]) - 1, max([max(c[i] for c in cubes) for i in range(3)]) + 1
vstd = set()
unvstd = [(cl,cl,cl)]

while unvstd:
    cube = unvstd.pop()
    unvstd += [s for s in (neighbors(cube)-cubes-vstd) if all(cl<=c<=cu for c in s)]
    vstd.add(cube)

print(sum([(s in vstd) for c in cubes for s in neighbors(c)])) # 2546

# import matplotlib.pyplot as plt
# ax = plt.figure().add_subplot(projection='3d')
# x,y,z = [[c[i] for c in cubes] for i in range(3)]
# ax.scatter(x,y,z)
# # xv,yv,zv = [[c[i] for c in vstd] for i in range(3)]
# # ax.scatter(xv,yv,zv)
# ax.set_xlabel('X');ax.set_ylabel('Y');ax.set_zlabel('Z')
# plt.show()