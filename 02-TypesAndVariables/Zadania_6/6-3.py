###
# A program that prints a university abbreviation
#   

# university = "Krakow University of Economics"
# print(university.strip())
# array = [university[0],university[7],university[21]]
# print(''.join(array))
# print()

def f(uniwersytet):
    array = uniwersytet[0], uniwersytet[7], uniwersytet[21]
    return ''.join(array)

if __name__ == "__main__":
    result = f("Krakow University of Economics")
    print(result)