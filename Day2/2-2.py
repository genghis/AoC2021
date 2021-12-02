input = [x.strip() for x in open('./input2-1.txt')]
horizontal = 0
depth = 0
aim = 0

for i in input:
    direction = i.split(' ')[0]
    value = int(i.split(' ')[1])
    if direction == 'forward':
        horizontal+=value
        depth+=(value*aim)
    elif direction == "up":
        aim-=value
    elif direction == "down":
        aim+=value

print(horizontal*depth)