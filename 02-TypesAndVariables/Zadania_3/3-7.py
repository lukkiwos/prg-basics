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
print("Northern Hemisphere in %: ", north/total*100)

print("Southern Hemisphere: ", south)
print("Southern Hemisphere in %: ", south/total*100)
print()




def f(polnoc, poludnie):
    total = 8000000000
    perc1 = polnoc/total*100
    perc2 = poludnie/total*100
    return perc1, perc2

if __name__ == "__main__":
    print(f"% of people in Northern and Southern Hemisphere is: {f(6000000000, 2000000000)}")