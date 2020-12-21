from aocutil import file_input

temp = file_input('day6.txt')
temp.append('')
group = []
groups = []

for line in temp:
    if line != '':
        person = set()
        for char in line:
            person.add(char)
        group.append(person)

    else:
        groups.append(group.copy())
        group.clear()


part1 = 0
part2 = 0

letters = 'qwertyuiopasdfghjklzxcvbnm'

for group in groups:
    anyone = set()
    everyone = {x for x in letters}

    for person in group:
        anyone = anyone | person
        everyone = everyone & person

    part1 += len(anyone)
    part2 += len(everyone)

print('Part 1 = {}\nPart 2 = {}'.format(part1, part2))