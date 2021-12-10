input = [x.strip() for x in open('input10-1.txt')]
# print(input)

legal = ['[]','()','{}','<>']
opens = ['[','(','{','<']
scores = {')': 3, ']': 57, '}': 1197,'>': 25137}
total = 0

string_list = []

def parse(string):
    for i in legal:
        if i in string:
            string = string.replace(i,'')
            return parse(string)
    if not string:
        return ''
    else:
        return string

for string in input:
    parsed = parse(string)
    result = list(filter(lambda x: x in scores.keys(), parsed))
    if not result:
        pass
    else:
        winner = result[0]
        total += scores[winner]

print(total)