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


def x_line(y1,y2,xcoord):
    if y1 > y2:
        high = y1+1
        low = y2
    else:
        high = y2+1
        low = y1
    for i in range(low,high):
        grid[i][xcoord] += 1

def y_line(x1,x2,ycoord):
    if x1 > x2:
        high = x1+1
        low = x2
    else:
        high = x2+1
        low = x1
    for i in range(low,high):
        grid[ycoord][i] += 1

for i in inputfile:
    if i[0][0] == i[1][0]:
        x_line(i[0][1],i[1][1],i[0][0])
    elif i[0][1] == i[1][1]:
        y_line(i[0][0],i[1][0],i[0][1])

answer_total = 0

for i in grid:
    answer_total += len([x for x in i if x > 1])

print(answer_total)