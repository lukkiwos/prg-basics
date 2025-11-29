###
# A program that reads temperature in degrees Celsius from the keyboard.
# Use comments to briefly describe the program's algorithm.
#
import math

# Read temrperature in Celcius degree from the keyboard
temp_1 = int(input("Enter the temperature in Celsius: "))

# Calculate the temperature in Kelvin and Fahrenheit
temp_2 = temp_1 + 273.15 # Kelvin
temp_3 = (temp_1 * 9/5) + 32 # Fahrenheit

# Print the values
print(f'The temperature in Celsius is: {temp_1}°C\n')
print(f'The temperature in Kelvin is: {temp_2}K\n')
print(f'The temperature in Fahrenheit is: {temp_3}°F\n')