def calc(operator, firstnumber, secondnumber):
    if operator == '+':
        return firstnumber + secondnumber
    elif operator == '-':
        return firstnumber - secondnumber
    elif operator == 'x' or operator == '*':
        return firstnumber * secondnumber
    elif operator == '/' or operator == 'div':
        return firstnumber / secondnumber
    else:
        print('Invalid parameters...')

with open('calc2.txt', 'r') as file:
    file_calc = file.read().splitlines()

repeat = False
i = 0
completed = []

while repeat == False:
    completed.append(file.calc[i])
    contents = file_calc[i].split(' ')
    if contents[1] == 'calc':
        i = calc(contents[2], contents[3], contents[4]) - 1
    else:
        i = contents[1] - 1