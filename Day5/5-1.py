inputfile = [x.strip().split('->') for x in open('./input5-1.txt')]

ymax = 0
xmax = 0

for i in inputfile:
    iloc = inputfile.index(i)
    for n in i:
        loc = i.index(n)
        inputfile[iloc][loc] = tuple(int(x) for x in n.strip().split(','))
        if inputfile[iloc][loc][0] > xmax:
            xmax = inputfile[iloc][loc][0]
        if inputfile[iloc][loc][1] > ymax:
            ymax = inputfile[iloc][loc][1]

gridline = []
for i in range(xmax+1):
    gridline.append(0)
grid = []
for i in range(ymax+1):
    grid.append(list(gridline))

def line(a1,a2,coord,axis):
    if a1 > a2:
        high = a1+1
        low = a2
    else:
        high = a2+1
        low = a1
    for i in range(low,high):
        if axis == 'x':
            grid[i][coord] += 1
        if axis == 'y':
            grid[coord][i] += 1

for i in inputfile:
    if i[0][0] == i[1][0]:
        line(i[0][1],i[1][1],i[0][0],'x')
    elif i[0][1] == i[1][1]:
        line(i[0][0],i[1][0],i[0][1],'y')

answer_total = 0

for i in grid:
    answer_total += len([x for x in i if x > 1])

print(answer_total)