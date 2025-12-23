###
# A program that reads temperature in degrees Celsius from the keyboard.
# Use comments to briefly describe the program's algorithm.
#

# Entering the temperature value in celsius
celsius = int(input("Enter temperature in Celsius:      "))

# Calculates kelvin and fahrenheit degrees
kelvin = celsius + 273.15
fahrenheit = celsius * 9/5 + 32

# Printing results
print(f"Temperature in Kelvin is:          {kelvin}K")
print(f"Temperature in Fahrenheit is:      {fahrenheit}°F")
print()



def f(temperature_celsius):
    temperature_in_kelvin = temperature_celsius + 273.15
    temperature_fahrenheit = temperature_celsius * 9/5 + 32
    return temperature_in_kelvin, temperature_fahrenheit


if __name__ == "__main__":
    print(f(0))