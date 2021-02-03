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
user_operator = str(input('Please provide an operator: '))
user_firstnumber = int(input('Please provide the first number: '))
user_secondnumber = int(input('Please provide the second number: '))
response = calc(user_operator, user_firstnumber, user_secondnumber)
print(response)