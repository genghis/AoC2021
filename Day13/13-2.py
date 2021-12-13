gridbasics = [x.strip() for x in open('input13.txt')]
# gridbasics = [x.strip() for x in open('testinput.txt')]
# gridbasics = [x.strip() for x in open('buddhainput.txt')]
gridcoordinates = []

folds = ['x=655','y=447','x=327','y=223','x=163','y=111','x=81','y=55','x=40','y=27','y=13','y=6']
# folds = ['y=7', 'x=5']

maxY = 0
maxX = 0
for i in gridbasics:
    a,b = i.split(',')
    if int(a) > maxX:
        maxX = int(a)
    if int(b) > maxY:
        maxY = int(b)
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
        for num in range(number):
            newlist = [a + b for a, b in zip(grid[num], grid[-num-1])]
            grid[num] = newlist
        grid = grid[:abs(number)]
        # print(len(grid))

    else:
        for index,line in enumerate(grid):
            newlist = []
            for ind,num in enumerate(line[0:number]):
                new = line[ind] + line[-ind-1]
                newlist.append(new)
            grid[abs(index)] = newlist
        # print(len(grid[index]))

total = 0
for ycoord,line in enumerate(grid):
    for xcoord,entry in enumerate(line):
        if entry != 0:
            total+=1
            grid[ycoord][xcoord] = '#'
        else:
            grid[ycoord][xcoord] = ' '
print('\n\n\n')
with open('output.txt', 'a') as f:
    for i in grid:
        f.write(''.join(i)+'\n')
    f.write('\n\n')
# print(total)