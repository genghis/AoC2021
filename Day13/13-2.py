gridbasics = [x.strip() for x in open('input13.txt')]
gridcoordinates = []

folds = ['x=655','y=447','x=327','y=223','x=163','y=111','x=81','y=55','x=40','y=27','y=13','y=6']

maxY = 894
maxX = 1310

for i in gridbasics:
    a,b = i.split(',')
    gridcoordinates.append((int(a),int(b)))

gridline = []
for i in range(maxX+1):
    gridline.append(0)
grid = []
for i in range(maxY+1):
    grid.append(list(gridline))

for i in gridcoordinates:
    xcoord = i[0]
    ycoord = i[1]
    grid[ycoord][xcoord] += 1

for i in folds:
    a,b = i.split('=')
    number = int(b)
    if a == 'y':
        total = 0
        print(f'Folding on Y. Grid is {len(grid)}, folding at {number}. This remainder should be 1: {len(grid)} - 2*{number} = {len(grid)-(2*number)} ')
        for num in range(number):
            newlist = [a + b for a, b in zip(grid[num], grid[-num-1])]
            grid[num] = newlist
        grid = grid[:abs(number)]

    else:
        total = 0
        print(f'Folding on X. Width is {len(grid[0])}, folding at {number}. This remainder should be 1: {len(grid[0])} - 2*{number} = {len(grid[0])-(2*number)}')
        for index,line in enumerate(grid):
            newlist = []
            for ind,num in enumerate(line[0:number]):
                new = line[ind] + line[-ind-1]
                newlist.append(new)
            grid[index] = newlist

total = 0
for ycoord,line in enumerate(grid):
    for xcoord,entry in enumerate(line):
        if entry:
            total+=1
            grid[ycoord][xcoord] = '#'
        else:
            grid[ycoord][xcoord] = ' '
print('\n\n\n')
with open('output.txt', 'a') as f:
    for i in grid:
        f.write(''.join(i)+'\n')
    f.write('\n\n')
print(total)