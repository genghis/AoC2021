draws = [67,31,58,8,79,18,19,45,38,13,40,62,85,10,21,96,56,55,4,36,76,42,32,34,39,89,6,12,24,57,93,47,41,52,83,61,5,37,28,15,86,23,69,92,70,27,25,53,44,80,65,22,99,43,66,26,11,72,2,98,14,82,87,20,73,46,35,7,1,84,95,74,81,63,78,94,16,60,29,97,91,30,17,54,68,90,71,88,77,9,64,50,0,49,48,75,3,59,51,33]

boards = [[]]
counter = 0
for i in open('./input4-1.txt'):
    i = i.strip()
    if i != '':
        boards[counter].append([int(x) for x in i.split(' ') if x != ''])
    else:
        counter += 1
        boards.append([])

bingo = False

while bingo == False:

    def winner_calc(winning_draw,board):
        winning_nums = []
        for i in board:
            for n in i:
                if type(n) == int:
                    winning_nums.append(n)
        print(f'{sum(winning_nums)}*{winning_draw}={sum(winning_nums)*winning_draw}')
        return True
        

    def check_for_winner(winning_draw):
        for n in boards:
            index_of_n = boards.index(n)
            bingo = list('x'*len(n[0]))
            for i in n:
                if bingo == i:
                    return winner_calc(winning_draw, n)
            for i in range(len(n)):
                vertical = [x[i] for x in n]
                if bingo == vertical:
                    return winner_calc(winning_draw, n)

    # print(boards)

    for i in draws:
        for n in boards:
            for o in n:
                print(f'{i}:::::{o}')
                if i in o:
                    o[o.index(i)] = 'x'
                    print(f'{i}:::::{o}')
        if check_for_winner(i) == True:
            bingo = True
            break