inputlist = [x.strip().split(' | ') for x in open('input8-1.txt')]

# mapping = {1: {'c','f'}, 4: {'b','c','d','f'}, 7: {'a','c','f'}, 8: {'a','b','c','d','e','f','g'}}
mapping = {1: 2, 4:4, 7:3, 8: 7}
counter = 0

for i in inputlist:
    # print(i[1])
    for n in i[1].split(' '):
        print(f'{n} is length {len(n)}')
        if len(n) in mapping.values():
            counter += 1

print(counter)