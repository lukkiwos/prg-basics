###
# A program that reads temperature in degrees Celsius from the keyboard.
# Use comments to briefly describe the program's algorithm.
#

temperature_celsius = int(input("Enter temperature in Celsius degrees: "))

temperature_kelvin = temperature_celsius + 273.15

temperature_fahrenheit = (temperature_celsius * 1.8) + 32

print(f"Temperature in Kelvin degrees: {temperature_kelvin:.2f}")
print(f"Temperature in Fahrenheit degrees: {temperature_fahrenheit:.2f}")