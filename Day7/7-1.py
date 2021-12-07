crabs = [int(x) for x in open('input7-1.txt').read().split(',')]

positions = {}

for i in range(max(crabs)+1):
    positions[i] = 0
    for crab in crabs:
        positions[i] += abs(crab-i)

print(min(positions.values()))