temperature = int(input('Inform the temperature (in C°): '))
temperatureInFahrenheit = (temperature * 1.8) + 32

print('-'*20)
print('Temperature in Celsius: {}C°'.format(temperature))
print('Temperature in Fahrenheit: {:.1f}F°'.format(temperatureInFahrenheit))
