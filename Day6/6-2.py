school = [int(x) for x in open('input6-1.txt').read().split(',')]
days = 256
feesh = {}

for day in range(days+1):
    feesh[day] = {}

for spawncounter in range(9):
    for day in feesh.keys():
        feesh[day][spawncounter] = 0

for fish in school:
    feesh[0][fish] += 1

for day in range(days):
    for spawncounter in range(9):
        print(feesh[day][spawncounter])
        if spawncounter == 0:
            feesh[day+1][spawncounter+6] += feesh[day][spawncounter]
            feesh[day+1][spawncounter+8] += feesh[day][spawncounter]
        else:
            feesh[day+1][spawncounter-1] += feesh[day][spawncounter]

print(sum(feesh[days].values()))