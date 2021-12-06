school = [int(x) for x in open('input6-1.txt').read().split(',')]

counter = 0
days = 80

def spawn():
    newfish = 0
    for index, fish in enumerate(school):
        if fish == 0:
            school[index] = 6
            newfish += 1
        else:
            school[index] -= 1
    for i in range(newfish):
        school.append(8)
    print(school)

while counter < days:
    spawn()
    counter += 1

print(len(school))