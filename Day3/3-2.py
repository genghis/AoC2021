input = [x.strip() for x in open('./input3-1.txt')]

def calc(numbers, starting, air):
    if len(numbers) == 1:
        return int(numbers[0],2)
    if air == "ox":
        a1 = 1
        a2 = 0
    else:
        a1=0
        a2=1
    position_list = [[],[]]
    for n in numbers:
        if n[starting] == "0":
            position_list[0].append(n)
        else:
            position_list[1].append(n)
    if len(position_list[0]) == len(position_list[1]) or len(position_list[1]) > len(position_list[0]):
        newnumbers = position_list[a1]
    else:
        newnumbers = position_list[a2]
    return calc(newnumbers, starting+1, air)

print(calc(input, 0, "ox")*calc(input, 0, "carb"))