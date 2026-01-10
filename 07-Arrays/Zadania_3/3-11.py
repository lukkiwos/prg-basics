array1 = [4, 36, 12, 28, 9, 44, 5]
array2 = [10, 3, 7, 1, 9]
array3 = [5, 4, 3, 2, 1]



def bubblesort(array):
    n = len(array)

    for i in range(n):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    return array


print("Original:", array1)
print("Sorted:", bubblesort(array1))
print()

print("Original:", array2)
print("Sorted:", bubblesort(array2))
print()

print("Original:", array3)
print("Sorted:", bubblesort(array3))