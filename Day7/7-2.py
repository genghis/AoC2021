# crabs = [int(x) for x in open('input7-1.txt').read().split(',')]
crabs = [1,2,3]
positions = {}

for i in range(max(crabs)+1):
    positions[i] = 0
    for crab in crabs:
        positions[i] += sum(range(abs(crab-i)+1))

print(min(positions.values()))
print(positions)