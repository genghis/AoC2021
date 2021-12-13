# gridbasics = [x.strip() for x in open('input13.txt')]
gridbasics = [x.strip() for x in open('testinput.txt')]
gridcoordinates = []

# folds = ['x=655']
folds = ['y=7', 'x=5']

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
        grid.pop(number)
        for num in range(number):
            newlist = [a + b for a, b in zip(grid[num], grid[-1])]
            # print(f'Adding {num} and {-num-1}')
            # print(grid[num])
            # print(grid[-1])
            # print(newlist)
            grid[num] = newlist
            grid.pop()
    else:
        for index,line in enumerate(grid):
            leftside = line[0:number]
            rightside = reversed(line[number+1::])
            newlist = [a + b for a, b in zip(leftside, rightside)]
            print(f'Adding chars 0 - {number} to {number+1} through end')
            print(leftside)
            print(rightside)
            print(newlist)
            grid[index] = newlist
    with open('output.txt', 'a') as f:
        for i in grid:
           f.write(str(i)+'\n')
    
    
total = 0
for line in grid:
    for entry in line:
        if entry != 0:
            total+=1
print('\n\n\n')
for i in grid:
    print(i)
# print(total)