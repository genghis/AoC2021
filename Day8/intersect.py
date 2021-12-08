
base = {
8: 'acedgfb',
5: 'cdfbe',
2: 'gcdfa',
3: 'fbcad',
7: 'dab',
9: 'cefabd',
6: 'cdfgeb',
4: 'eafb',
0: 'cagedb',
1: 'ab'}

# print(base[8])

for v in base:
    for i in base:
        print(f'{v} and {i} share {len(set(base[v]).intersection(base[i]))}')