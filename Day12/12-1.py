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

def find_all_paths(caves, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if start not in caves.keys():
            return []
        paths = []
        for cavern in caves[start]:
            if cavern.islower() and cavern in path:
                pass
            else:
                newpaths = find_all_paths(caves, cavern, end, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths

answer = find_all_paths(caves,'start','end',[])

print(len(answer))