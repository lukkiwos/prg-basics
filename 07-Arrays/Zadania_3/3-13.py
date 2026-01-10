array = [15, 38, 7, 23, 14]

number = int(input("Number: "))
print(f"Array: {", ".join(map(str, array))}")

def occurs(number, array):
    for x in array:
        if x == number:
            return True
    return False
    

if occurs(number, array):
    print(f"Result: number {number} appears in the array")
else:
    print(f"Result: number {number} does not appears in the array")





