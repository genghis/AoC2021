input = [int(x.strip()) for x in open('./input1-1.txt')]
chunks_list = [input[x]+input[x+1]+input[x+2] for x in range(len(input[:-2:])) if x < len(input)-1]
print(len([v for i, v in enumerate(chunks_list) if v > chunks_list[i-1] and i !=0]))