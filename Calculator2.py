def calc(operator, firstnumber, secondnumber):
    if operator == '+':
        return firstnumber + secondnumber
    elif operator == '-':
        return firstnumber - secondnumber
    elif operator == 'x' or operator == '*':
        return firstnumber * secondnumber
    elif operator == '/' or operator == 'div':
        return firstnumber / secondnumber
    elif operator == 'pow':
        return firstnumber ^ secondnumber
    else:
        print('Invalid parameters...')

with open('calc.txt', 'r') as file:
    file_calc = file.read().splitlines()

answers = []

for iterator in range(0, len(file_calc)):
    contents = file_calc[iterator].split(' ')
    answers.append(calc(str(contents[1]), int(contents[2]), int(contents[3])))
print(sum(answers))