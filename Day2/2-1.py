input = [x.strip() for x in open('./input2-1.txt')]
x = 0
y = 0

for i in input:
    direction = i.split(' ')[0]
    value = int(i.split(' ')[1])
    if direction == 'forward':
        x+=value
    elif direction == "up":
        y-=value
    elif direction == "down":
        y+=value

print(x*y)