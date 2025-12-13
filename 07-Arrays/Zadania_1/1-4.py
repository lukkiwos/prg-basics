###
# Prints some array elements
#

arr = [2, 3, 7, 5, 4]

print("1 ---- ", arr)                                                      # 1


print('2 ---- Number of elements', len(arr))                           # 2


print('3 ---- First value', arr[0])                                    # 3


print('4 ---- Second value', arr[1])                                   # 4


print('5 ---- Last value', arr[-1])                                    # 5


n = len(arr)                                                    # 6
print('6 ---- Last but one value', arr[n-2])                          


print('7 ---- Sum of the first and last value', arr[0] + arr[-1])      # 7


print('8 ---- Middle value', arr[len(arr)//2])                         # 8


array = [0]                                                     # 9
for i in arr:
    
    print(i, end = ' ')
print('All array values separated')                            



# to read the last value of an array 
# use array[len(array)-1] or array[-1]