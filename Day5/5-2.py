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

def direction(start, end):
    if start < end:
        difference = abs(start-end)
        return ["add",difference+1]
    else:
        difference = abs(start-end)
        return ["sub",difference+1]

def list_create(start, end):
    payload = direction(start, end)
    if payload[0] == "add":
        return [start+x for x in range(payload[1])]
    else:
        return [start-x for x in range(payload[1])]

for i in inputfile:
    start = i[0]
    end = i[1]
    xlist = list_create(start[0], end[0])
    ylist = list_create(start[1], end[1])
    if len(xlist) > len(ylist):
        ylist = [ylist[0] for x in range(len(xlist))]
    if len(ylist) > len(xlist):
        xlist = [xlist[0] for x in range(len(ylist))]
    for i in zip(ylist,xlist):
        y = i[0]
        x = i[1]
        grid[y][x] += 1

answer_total = 0

for i in grid:
    answer_total += len([x for x in i if x > 1])

print(answer_total)