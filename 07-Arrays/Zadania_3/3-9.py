array = [
    (["water", "book", "sky"], ["water", "book", "sky"]),
    ([True, False], [True, False, True]),
    ([5, 3, 1], [5, 3, 1]),
    ([3, 2, 1], [3, 2]),
]


def compare(array1, array2):
    if len(array1) != len(array2):
        return False
    
    i = 0
    
    while i < len(array1):
        if array1[i] != array2[i]:
            return False
        i += 1
    
    return True



for array1, array2 in array:
    
    print("Array1: ", ", ".join(str(x) for x in array1))
    
    print("Array2: ", ", ".join(str(x) for x in array2))

    if compare(array1, array2):
        print("Comparison: Arrays are the same")
    else:
        print("Comparison: Arrays are different")

    print()
