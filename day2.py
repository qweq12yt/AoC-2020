from aocutil import file_input

temp = file_input('day2.txt')
passwords = []

for line in temp:
    split = line.split()
    entry = [None, None, None, None]
    num = split[0].split(sep='-')
    entry[1] = int(num[0])
    entry[2] = int(num[1])
    entry[0] = split[1][0]
    entry[3] = split[2]
    passwords.append(entry)

n = 0
m = 0
for entry in passwords:
    char = entry[0]
    i = entry[1]
    j = entry[2]
    password = entry[3]
    part2 = False
    if i <= password.count(char) <= j:
        n += 1
    if password[i - 1] == char:
        part2 = not part2
    if password[j - 1] == char:
        part2 = not part2
    if part2:
        m += 1

print('Part 1 = {}\nPart 2 = {}'.format(n, m))
