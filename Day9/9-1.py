input = [list(x.strip()) for x in open('input9-1.txt')]
for i in input:
    for index,n in enumerate(i):
        i[index] = int(n)

risk = 0

for line_location, line in enumerate(input):
    
    if line_location == 0:
        previous_line = []
        previous_line.extend([10 for i in range(len(line))])
        next_line = input[line_location+1]
    elif line_location == len(input)-1:
        next_line = []
        next_line.extend([10 for i in range(len(line))])
        previous_line = input[line_location-1]
    else:
        previous_line = input[line_location-1]
        next_line = input[line_location+1]
    for i,val in enumerate(line):
        if i == 0:
            previous_item = 10
        else:
            previous_item = line[i-1]
        if i == len(line)-1:
            next_item = 10
        else:
            next_item = line[i+1]
        if val < previous_line[i] and val < next_line[i] and val < previous_item and val < next_item:
            risk += val+1

print(risk)