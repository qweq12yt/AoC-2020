from aocutil import file_input


def checkhex(string):
    n = '0x' + string
    try:
        n = float.fromhex(n)
        return True
    except ValueError:
        return False


temp = file_input('day4.txt')
temp.append('')

string = ''
passports = []
for line in temp:
    if line != '':
        string += line + ' '
    else:
        data = string.split()
        entry = dict()
        for field in data:
            key, value = field.split(sep=':')
            entry[key] = value
        passports.append(entry)
        string = ''

fields = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')
n = [0, 0]
for passport in passports:
    flag1 = True
    for check in fields:
        if passport.get(check) is None:
            flag1 = False
            break

    flag2 = True
    for check in fields:
        value = passport.get(check)

        if value is None:
            flag2 = False
            break
        if check == 'byr':
            if len(value) != 4 or not (1920 <= int(value) <= 2020):
                flag2 = False
                break
        if check == 'iyr':
            if len(value) != 4 or not (2010 <= int(value) <= 2020):
                flag2 = False
                break
        if check == 'eyr':
            if len(value) != 4 or not (2020 <= int(value) <= 2030):
                flag2 = False
                break
        if check == 'hgt':

            if value.isdecimal():
                flag2 = False
                break

            if 'cm' in value:
                if not (150 <= int(value.strip('cm')) <= 193):
                    flag2 = False
                    break

            elif 'in' in value:
                if not (59 <= int(value.strip('in')) <= 76):
                    flag2 = False
                    break

            else:
                flag2 = False
                break
        if check == 'hcl':
            if value[0] != '#' or len(value) != 7 or not checkhex(value[1:]):
                flag2 = False
                break
        if check == 'ecl':
            if value not in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
                flag2 = False
                break
        if check == 'pid':
            if len(value) != 9 or not value.isdecimal():
                flag2 = False
                break

    if flag1:
        n[0] += 1

    if flag1 and flag2:
        print(passport['eyr'])
        n[1] += 1
print()
print(n)
