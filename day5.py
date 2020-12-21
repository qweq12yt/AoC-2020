from aocutil import file_input

l = file_input('day5.txt')
highest = 0
ids = []

for line in l:
    row_max = 127
    row_min = 0
    col_max = 7
    col_min = 0

    for char in line:
        if char == 'F':
            row_max = row_max - 1 - (row_max - row_min) // 2
        if char == 'B':
            row_min = (row_min + row_max + 1) // 2

        if char == 'L':
            col_max = col_max - 1 - (col_max - col_min) // 2
        if char == 'R':
            col_min = (col_min + col_max + 1) // 2

    seat_id = row_max * 8 + col_max
    ids.append(seat_id)
    if seat_id > highest:
        highest = seat_id

ids.sort()

prev = None
for n in ids:
    if prev is None:
        prev = n
    else:
        if prev - n == -1:
            prev = n
        else:
            break

print('Part 1 = {}\nPart 2 = {}'.format(highest, prev + 1))
