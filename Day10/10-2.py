input = [x.strip() for x in open('input10-1.txt')]

legal = ['[]','()','{}','<>']
scores = {')': 1, ']': 2, '}': 3,'>': 4}
matching = {'[':']','(':')','{':'}','<':'>'}
total = []

def parse(string):
    for i in legal:
        if i in string:
            string = string.replace(i,'')
            return parse(string)
    if not string:
        return ''
    else:
        return string

def complete(string):
    internal_score = 0
    l1 = []
    for i in string[::-1]:
        l1.append(matching[i])
    for n in l1:
        internal_score *= 5
        internal_score += scores[n]
    total.append(internal_score)
    
for string in input:
    parsed = parse(string)
    if parsed == '':
        pass
    result = list(filter(lambda x: x in scores.keys(), parsed))
    if not result:
        complete(parsed)
    else:
        winner = result[0]
        
total.sort()
total_index = int(len(total)/2 - .5)
print(total[total_index])