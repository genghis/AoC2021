#abandoned this, but working on it made me realize I was setting my maxy/maxx based on DOTS, not based on PAPER

gridbasics = [x.strip() for x in open('input13.txt')]
folds = ['x=655','y=447','x=327','y=223','x=163','y=111','x=81','y=55','x=40','y=27','y=13','y=6']

occupied = set()
maxY = 0
maxX = 0

for i in gridbasics:
    a,b = i.split(',')
    if int(a) > maxX:
        maxX = int(a)
    if int(b) > maxY:
        maxY = int(b)
    occupied.add((int(a),int(b)))

print(occupied)
for fold in folds:
    axis = fold.split('=')[0]
    number = fold.split('=')[1]
    for tup in occupied:
        pass
