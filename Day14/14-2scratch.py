starting = open('testinput.txt').read().split('\n')
template = starting.copy()[0]
rules = starting.copy()[2::]

turns = 40
window = 2
rulesdict = {}
answer = {}

for i in rules:
    pair,intruder = i.split(' -> ')
    rulesdict[pair] = intruder
    answer[intruder] = 0

print(answer)

for letter in template:
    answer[letter] += 1

def calculate(letters,number):
    if number > 0:
        newletter = rulesdict[letters]
        answer[newletter] += 1
        newpairs = [letters[0]+newletter,newletter+letters[1]]
        for pair in newpairs:
            calculate(pair,number-1)

for i in range(len(template)-1):
    print(template[i])
    calculate(template[i]+template[i+1], turns)

print(answer)