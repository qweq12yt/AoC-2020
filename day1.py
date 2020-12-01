from aocutil import file_input
entry = file_input('day1.txt', int)
for i in range(len(entry)):
    for j in range(i + 1):
        sums = entry[i] + entry[j]
        if sums == 2020:
            print('1/2:\n{0} + {1} = 2020\n{0} + {1} = {2}'.format(entry[i], entry[j], entry[i] * entry[j]))

for i in range(len(entry)):
    for j in range(i + 1):
        for k in range(j + 1):
            sums = (entry[i] + entry[j] + entry[k])
            if sums == 2020:
                print('2/2\n{0} + {1} + {2} = 2020\n{0} * {1} * {2} = {3}'.format(entry[i], entry[j], entry[k], entry[i] * entry[j] * entry[k]))
