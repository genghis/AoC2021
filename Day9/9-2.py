input = [[int(y) for y in x.strip()] for x in open('input9-1.txt')]

basin_seeds = {}
spoken_for = []

def up(y,x):
    if (y-1,x) in spoken_for:
        return False
    elif y == 0:
        return False
    elif input[y-1][x] == 9:
        return False
    else:
        return True
def down(y,x):
    if (y+1,x) in spoken_for:
        return False
    elif y == len(input)-1:
        return False
    elif input[y+1][x] == 9:
        return False
    else:
        return True
def left(y,x):
    if (y,x-1) in spoken_for:
        return False
    elif x == 0:
        return False
    elif input[y][x-1] == 9:
        return False
    else:
        return True
def right(y,x):
    if (y,x+1) in spoken_for:
        return False
    elif x == len(input[y])-1:
        return False
    elif input[y][x+1] == 9:
        return False
    else:
        return True

def size_calc(y,x):
    total = 0
    spoken_for.append((y,x))
    if up(y,x):
        total += 1+size_calc(y-1,x)
    if down(y,x):
        total += 1+size_calc(y+1,x)
    if left(y,x):
        total += 1+size_calc(y,x-1)
    if right(y,x):
        total += 1+size_calc(y,x+1)
    return total

for line_location, line in enumerate(input):
    if line_location == 0:
        previous_line = []
        previous_line.extend([10 for i in range(len(line))])
        next_line = input[line_location+1]
    elif line_location == len(input)-1:
        next_line = []
        next_line.extend([10 for i in range(len(line))])
        previous_line = input[line_location-1]
    else:
        previous_line = input[line_location-1]
        next_line = input[line_location+1]
    for i,val in enumerate(line):
        if i == 0:
            previous_item = 10
        else:
            previous_item = line[i-1]
        if i == len(line)-1:
            next_item = 10
        else:
            next_item = line[i+1]
        if val < previous_line[i] and val < next_line[i] and val < previous_item and val < next_item:
            basin_seeds[f"{line_location}|{i}"] = 1 # set dictionary key with y and x coordinates

for seed in basin_seeds:
    y,x = seed.split('|')
    y,x = int(y),int(x)
    size = size_calc(y,x)
    basin_seeds[seed] += size

answer = list(basin_seeds.values())
answer.sort()

print(answer[-1]*answer[-2]*answer[-3])