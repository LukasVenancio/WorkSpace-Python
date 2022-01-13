originalValue = int(input('What is the original value of the product? $'))
desiredDiscount = int(input('What is the desired discount for this product (in percentage)?'))
newValue = originalValue - (originalValue * (desiredDiscount / 100))

print('-'*20)
print('Original value: ${}'.format(originalValue))
print('Desired discount: {}%'.format(desiredDiscount))
print('-'*20)
print('New value: ${}'.format(newValue))
