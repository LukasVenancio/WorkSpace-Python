multiplicand = int(input('What is the multiplicand?'))
maximumMultiplier = int(input('What is the maximum multiplier?'))

i = 0
while (i <= maximumMultiplier):
    print('{} X {} = {}'.format(multiplicand, i, multiplicand * i))
    i += 1
