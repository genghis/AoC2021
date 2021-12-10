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
    total = 0
    for i in string[::-1]:
        total *= 5
        total += scores[matching[i]]
    total.append(total)
    
for string in input:
    parsed = parse(string)
    if parsed == '':
        pass
    result = list(filter(lambda x: x in scores.keys(), parsed))
    if not result:
        complete(parsed)
        
total.sort()
total_index = int(len(total)/2 - .5)
print(total[total_index])