inputlist = [x.strip().split(' | ') for x in open('input8-1.txt')]

mapping = {1: 2, 4:4, 7:3, 8: 7}
counter = 0

for i in inputlist:
    for n in i[1].split(' '):
        if len(n) in mapping.values():
            counter += 1

print(counter)