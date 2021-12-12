inputlist = [x.strip() for x in open('input12.txt')]

caves = {}

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

def traverse(caves, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        paths = []
        for cavern in caves[start]:
            if cavern.islower() and cavern in path:
                pass
            else:
                newpaths = traverse(caves, cavern, end, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths

answer = traverse(caves,'start','end',[])

print(len(answer))