with open('input7-1.txt') as crabshack: 
    crabs = [int(x) for x in crabshack.read().split(',')] 
    print(min({k:v for k in range(max(crabs)+1) for v in [sum(sum(range(abs(x-k)+1)) for x in crabs) for x in crabs]}.values()))