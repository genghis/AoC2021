input = [int(x.strip()) for x in open('./input1-1.txt')]
print(len([v for i, v in enumerate(input) if v > input[i-1] and i !=0]))