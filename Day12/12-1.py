inputlist = [x.strip() for x in open('testinput.txt')]
# print(inputlist)

caves = {}
current_path = []
paths = []

for i in inputlist:
    a,b = i.split('-')
    if a in caves.keys():
        caves[a].append(b)
    else:
        caves[a] = [b]
    if b in caves.keys():
        caves[b].append(a)
    else:
        caves[b] = [a]


# print(caves)
def traverse(cave):  
    if cave == 'end':
        pass
    else:
        for i in caves[cave]:
            if i.islower() and i in current_path:
                pass
            elif 'end' in current_path:
                pass
            else:
                current_path.append(i)
                traverse(i)
    if current_path[0] == 'start' and current_path[-1] == 'end':
        paths.append(current_path.copy())

for cave in caves['start']:
    current_path.clear()
    current_path = ['start',cave]
    traverse(cave)

print(paths)