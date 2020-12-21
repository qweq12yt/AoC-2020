"""Loads a text file from disk and returns every single line as a entry in a list"""


def file_input(file_name, convert=str, matrix=False):
    file = open(file_name, 'r')
    data = []
    if matrix:
        for line in file:
            l = []
            for char in line:
                if char != '\n':
                    l.append(convert(char))
            data.append(l)
    else:
        for line in file:
            data.append(convert(line.strip('\n')))
    file.close()
    return data.copy()


"""Loads a file and returns the first line separated according to the parameter sep"""


def file_input_line(file_name, sep=' ', key=str, strip=''):
    file = open(file_name, 'r').readline().strip(strip)
    data = []
    file = file.split(sep)
    for item in file:
        data.append(key(item))
    return data.copy()


"""Prints any 2d list (matrix). Needs a 2d as input"""


def print_grid(grid):
    string = ''
    for line in grid:
        l = ''
        for char in line:
            l += str(char)
        string += l + '\n'
    print(string)
