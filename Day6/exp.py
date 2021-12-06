school = [int(x) for x in open('testinput.txt').read().split(',')]

counter = 0
days = 256
totalfish = 0
feesh = {}

for i in range(19):
    feesh[i] = 0

for i in school:
    feesh[i] += 1

print(feesh)

for i in range(19):
    if i+9 <= 18:
        feesh[i+9] += feesh[i]
    if i+7 <= 18:
        feesh[i+7] += feesh[i]

print(sum(feesh.values()))
# print(feesh)

#26984457539
#716637672776