def second_largest(array):          # 1
    biggest = array[0]
    
    for x in array:
        if x > biggest:
            biggest = x

    second_biggest = array[0]
    for x in array:
        if x > second_biggest and x < biggest:
            second_biggest = x
    
    return second_biggest


def difference(array):              # 2
    largest = array[0]
    
    for x in array:
        if x > largest:
            largest = x
    
    smallest = array[0]

    for x in array:
        if x < smallest:
            smallest = x

    difference = largest - smallest

    return difference


def median(array):                  # 3
    n = len(array)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    
    if len(array) % 2 != 0:
        mediana = array[len(array) // 2]
    
    return mediana


def two_element(array):             # 4
    array1 = []

    biggest = array[0]
    smallest = array[0]

    for x in array:
        if x > biggest:
            biggest = x

    for x in array:
        if x < smallest:
            smallest = x

    array1.append(smallest)
    array1.append(biggest)

    return array1


def string(array):
    string1 = ""
    
    for x in array:
        x = str(x)
        string1 += x
        if x != str(array[len(array) - 1]):
            string1 += "-"

    return string1



array = [7, 3, 8, 5, 2]

print("Numbers: ", ", ".join(map(str, array)))
print(f"Second largest number: {second_largest(array)}")
print(f"Median: {median([7, 3, 8, 5, 2])}")
print("Smallest and largest number: ", ", ".join(map(str, two_element([7, 3, 8, 5, 2]))))
print(f"Numbers as a string: {string([7, 3, 8, 5, 2])}")