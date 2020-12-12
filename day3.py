from aocutil import file_input

grid = file_input('day3.txt', matrix=True)

slopes = [0, 0, 0, 0, 0]
for i in range(len(grid)):
    mode1 = i % len(grid[0])
    mode2 = (i * 3) % len(grid[0])
    mode3 = (i * 5) % len(grid[0])
    mode4 = (i * 7) % len(grid[0])
    mode5 = i % len(grid[0])

    if grid[i][mode1] == '#':
        slopes[0] += 1
    if grid[i][mode2] == '#':
        slopes[1] += 1
    if grid[i][mode3] == '#':
        slopes[2] += 1
    if grid[i][mode4] == '#':
        slopes[3] += 1
    if i * 2 < len(grid) and grid[i * 2][mode5] == '#':
        slopes[4] += 1

print('Part 1 = {}\nPart 2 = {}'.format(slopes[1], slopes[0] * slopes[1] * slopes[2] * slopes[3] * slopes[4]))