x = 2
y = 2
z = 2
n = 2

xyz = []
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            if sum([i, j, k]) != n:
                xyz.append([i, j, k])
print(xyz)

xyz = []
xyz = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1)
       if sum([i, j, k]) != n]
print(xyz)
