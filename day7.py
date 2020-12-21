from aocutil import file_input

temp = file_input('day7.txt')
rules = []
for i in range(len(temp)):
    rule = []
    temp[i] = temp[i].split(' bags contain ')
    for j in range(len(temp[i])):
        temp[i][j] = temp[i][j].split('bag')
        for k in temp[i][j]:
            rule.append(k)

    for k in range(len(rule)):
        rule[k] = rule[k].replace('bag', '')
        rule[k] = rule[k].replace(',', '')
        rule[k] = rule[k].replace(', ', '')
        rule[k] = rule[k].replace('s.', '')
        rule[k] = rule[k].replace('s ', '')
        rule[k] = rule[k].replace('.', '')
        rule[k] = rule[k].strip()
        if rule[k] == 'no other':
            rule[k] = None

    try:
        rule.remove('')
    except ValueError:
        pass

    for j in range(1, len(rule)):
        if rule[1] is not None:
            rule[j] = (int(rule[j][0]), rule[j][2:])

    rules.append(tuple(rule))

reverse_graph = dict()
for rule in rules:
    for i in range(1, len(rule)):
        if rule[i] is not None:
            if rule[i][1] not in reverse_graph:
                reverse_graph[rule[i][1]] = [(rule[0], rule[i][0])]
            else:
                reverse_graph[rule[i][1]].append((rule[0], rule[i][0]))

graph = dict()
for rule in rules:
    graph[rule[0]] = rule[1:]

print(graph)
print(reverse_graph)

# TODO