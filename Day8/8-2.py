inputlist = [x.strip().split(' | ') for x in open('input8-1.txt')]

easy_mapping = {1:2, 4:4, 7:3, 8:7}
answer = 0

for i in inputlist:
    n_list = []
    local_answer=''
    local_mapping = {}
    for k,v in easy_mapping.items():
        for n in i[0].split(' '):
            if v == len(n):
                local_mapping[k] = n
    for n in i[0].split(' '):
        if len(n) == 5:
            if len(set(n).intersection(local_mapping[7])) == 3 and len(set(n).intersection(local_mapping[1])) == 2:
                local_mapping[3] = n
            elif len(set(n).intersection(local_mapping[4])) == 2:
                local_mapping[2] = n
            else:
                local_mapping[5] = n
        elif len(n) == 6:
            if len(set(n).intersection(local_mapping[1])) == 1 and len(set(n).intersection(local_mapping[7])) == 2:
                local_mapping[6] = n
            elif len(set(n).intersection(local_mapping[4])) == 4:
                local_mapping[9] = n
            else:
                local_mapping[0] = n
    for n in i[1].split(' '):
        for k,v in local_mapping.items():
            if set(n) == set(v):
                n_list.append(str(k))
    answer += int(''.join(n_list))
print(answer)