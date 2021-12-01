input = [int(x.strip()) for x in open('./input1-1.txt')]
windowsize = 3
chunks_list = [sum(input[x:x+windowsize]) for x in range(len(input[:-2:])) if x < len(input)-1]
print(len([v for i, v in enumerate(chunks_list) if v > chunks_list[i-1] and i !=0]))