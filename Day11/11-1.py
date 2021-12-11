grid = [[int(y) for y in x.strip()] for x in open('input11-1.txt')]
flashes = []
steps = 0
target = 100

def flash(octobro):
    flashes.append(octobro)
    ycoord = octobro[0]
    xcoord = octobro[1]
    surrounding = []
    listy = [x for x in range(ycoord-1,ycoord+2) if 10 > x >= 0]
    listx = [x for x in range(xcoord-1,xcoord+2) if 10 > x >= 0]
    for ycoordinate in listy:
        for xcoordinate in listx:
            surrounding.append((ycoordinate,xcoordinate))
    for octo in surrounding:
        y = octo[0]
        x = octo[1]
        if grid[y][x] > 9:
            pass
        else:
            grid[y][x] += 1
            if grid[y][x] > 9:
                flash((y,x))

def step():
    flashbros = []
    for ycoord, line in enumerate(grid):
        for xcoord, octopus in enumerate(line):
            if octopus >= 10:
                grid[ycoord][xcoord] = 0
            grid[ycoord][xcoord] += 1
            if grid[ycoord][xcoord] >= 10:
                flashbros.append((ycoord,xcoord))
    for octobro in flashbros:
        flash(octobro)
    

while steps < target:
    step()
    steps += 1

print(len(flashes))