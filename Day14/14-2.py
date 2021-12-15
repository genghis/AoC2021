from collections import Counter
import re

starting = open('input14.txt').read().split('\n')
template = starting.copy()[0]
rules = starting.copy()[2::]

turns = 10
window = 2
rulesdict = {}

for i in rules:
    pair,intruder = i.split(' -> ')
    rulesdict[pair] = f'{pair[0]}{intruder}{pair[1]}'

def invade(molecule):
    molecule = "".join([rulesdict[c] if c in rulesdict else c for c in molecule])
    return molecule


count = 0

while count < turns:
    template = invade(template)
    count += 1
    print(count)

howmany = Counter(template)
print(template)
most = howmany.most_common()[0]
least = howmany.most_common()[-1]

print(most[1]-least[1])
# print(rulesdict)