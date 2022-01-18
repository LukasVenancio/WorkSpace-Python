import random
from math import sqrt
import emoji

#Returns the square root of the typed number
number = int(input('Type any number: '))
squareRoot = sqrt(number)

print(squareRoot)

print('='*40)

#Raffle an integer number
randomNumber = random.randint(1, 10)
print(randomNumber)

print('='*40)

#Draw an emoji
print(emoji.emojize('I am the master of spinal pain :sunglasses: !'))
