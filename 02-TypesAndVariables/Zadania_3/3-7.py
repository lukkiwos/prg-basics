###
# A program that calculates and prints:
# - the number of people and percentage of the total
#   population living in the Northern Hemisphere
# - the number of people and percentage of the total
#   population living in the Southern Hemisphere
#
total = 8000000000

north = 7200000000
south = total - north

print("World population: ", total)

print("Northern Hemisphere: ", north)
print(f"Northern Hemisphere in %: {north/total*100:.0f}")

print(f"Southern Hemisphere: {south}")
print(f"Southern Hemisphere in %: {south/total*100:.0f}")