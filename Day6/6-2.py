school = [int(x) for x in open('input6-1.txt').read().split(',')]
days = 256
feesh = {}

for i in range(days+1):
    feesh[i] = {}

for i in range(9):
    for day in feesh.keys():
        feesh[day][i] = 0

for i in school:
    feesh[0][i] += 1

for i in range(days):
    for n in range(9):
        print(feesh[i][n])
        if n == 0:
            feesh[i+1][n+6] += feesh[i][n]
            feesh[i+1][n+8] += feesh[i][n]
        else:
            feesh[i+1][n-1] += feesh[i][n]

print(sum(feesh[days].values()))