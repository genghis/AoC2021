#I did this after hours of struggling with the other way (13-2.py). Once I got that to work, I came back to this and it took like 20 minutes, because I am NOT a smart man.
gridbasics = [x.strip() for x in open('input13.txt')]
folds = ['x=655','y=447','x=327','y=223','x=163','y=111','x=81','y=55','x=40','y=27','y=13','y=6']

occupied = set()
maxY = 1310
maxX = 894
minY = 6
minX = 40

for i in gridbasics:
    a,b = i.split(',')
    occupied.add((int(a),int(b)))

for fold in folds:
    tempset = occupied.copy()
    axis = fold.split('=')[0]
    number = fold.split('=')[1]
    number = int(number)
    if axis == 'y': 
        for tup in tempset:
            if tup[1] > number:
                newnum = number*2-tup[1]
                newtup = (tup[0],newnum)
                occupied.add(newtup)
                occupied.remove(tup)
    elif axis == 'x': 
        for tup in tempset:
            if tup[0] > number:
                newnum = number*2-tup[0]
                newtup = (newnum,tup[1])
                occupied.add(newtup)
                occupied.remove(tup)
    
grid = []
for num in range(minY):
    grid.append([' ' for x in range(minX)])

for tup in occupied:
    grid[tup[1]][tup[0]] = '#'

with open('output.txt', 'a') as f:
    for i in grid:
        f.write(''.join(i)+'\n')
    f.write('\n\n')
