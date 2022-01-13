print('Hi ' * 20)

name = input('What is your name?')
print('Nice to meet you, {}!'.format(name))
print('Nice to meet you, {:20}!'.format(name))
print('Nice to meet you, {:>20}!'.format(name))
print('Nice to meet you, {:<20}!'.format(name))
print('Nice to meet you, {:^20}!'.format(name))
print('Nice to meet you, {:*^20}!'.format(name))

firstNumber = int(input('What is the first number?'))
secondNumber = int(input('What is the second number?'))

sum = firstNumber + secondNumber
subtraction = firstNumber - secondNumber
multiplication = firstNumber * secondNumber
division = firstNumber / secondNumber
potentiation = firstNumber ** secondNumber
entireDivision = firstNumber // secondNumber
divisionRemainder = firstNumber % secondNumber

print('The sum of the numbers is: {}'.format(sum))
print('The subtraction of the numbers is: {}'.format(subtraction))
print('The multiplication of the numbers is: {}'.format(multiplication))
print('The division of the numbers is: {:.1f}'.format(division))
print('The potentiation of the numbers is: {}'.format(potentiation))
print('The entire division of the numbers is: {}'.format(entireDivision))
print('The division remainder of the numbers is: {}'.format(divisionRemainder))
