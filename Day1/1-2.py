input = [int(x.strip()) for x in open('./input1-1.txt')]
chunks_list = []

for i in range(len(input[:-2:])):
    if i < len(input)-1:
        chunks_list.append(input[i]+input[i+1]+input[i+2])

print(len([v for i, v in enumerate(chunks_list) if v > chunks_list[i-1] and i !=0]))