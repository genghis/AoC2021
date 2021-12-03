input = [x.strip() for x in open('./input3-1.txt')]

total_dict = {}

for n in range(len(input[0])):
    total_dict[n+1] = [0,0]
    for i in input:
        if i[n] == '0':
            total_dict[n+1][0] += 1
        else:
            total_dict[n+1][1] += 1

gamma_rate = ''
epsilon_rate = ''

for k in total_dict.keys():
    gamma_rate += str(total_dict[k].index(max(total_dict[k])))
    epsilon_rate += str(total_dict[k].index(min(total_dict[k])))

int_gamma = int(gamma_rate,2)
int_epsilon = int(epsilon_rate,2)

print(int_gamma*int_epsilon)