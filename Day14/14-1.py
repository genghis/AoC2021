from collections import Counter

starting = open('testinput.txt').read().split('\n')
template = starting.copy()[0]
rules = starting.copy()[2::]

turns = 40
window = 2
rulesdict = {}

for i in rules:
    pair,intruder = i.split(' -> ')
    rulesdict[pair] = f'{pair[0]}{intruder}{pair[1]}'

def invade(molecule):
    templist = []
    for n in range(len(molecule)-1):
        chunk = molecule[n:n+window]
        if n == len(molecule)-2:
            templist.append(rulesdict[chunk])
        else:
            templist.append(rulesdict[chunk][:2])
    return ''.join(templist)

count = 0

while count < turns:
    template = invade(template)
    count += 1
    print(count)

howmany = Counter(template)

most = howmany.most_common()[0]
least = howmany.most_common()[-1]

print(most[1]-least[1])