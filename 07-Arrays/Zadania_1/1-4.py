###
# Prints some array elements
#

arr = [2, 3, 7, 5, 4]

print(arr)

print('Number of elements', len(arr))

print('First value', arr[0])

print('Second value', arr[1])

print('Last value', arr[-1])

n = len(arr)
print('Last but one value', arr[n-2])

print('Sum of the first and last value', arr[0] + arr[-1])

print('Middle value', arr[len(arr)//2])

array = [0]
for i in arr:
    
    print(i, end = ' ' )
print('All array values separated',)