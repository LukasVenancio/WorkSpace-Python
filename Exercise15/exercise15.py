print('==========PRICE TABLE==========')
print('Price per day rented: $60')
print('Price per kilometer traveled: $0.15')
print('===============================')

totalDays = int(input('For who many days was the car rented? '))
traveledKilometers = int(input('Traveled kilometers: '))
finalPrice = (totalDays * 60) + (traveledKilometers * 0.15)

print('='*30)
print('The total price is: ${}'.format(finalPrice))
