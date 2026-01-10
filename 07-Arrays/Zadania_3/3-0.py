import random

arr1 = [3,7,1,0,4]
print(arr1)
print()

arr2 = [[2,3],[7,1],[0,4]]
print(arr2)
print()

arr3 = [7 for i in range(5)]
print(arr3)
print()

arr4 = [i for i in range(1,10)]
print(arr4)
print()

arr5 = [i*2 for i in range(1,10)]
print(arr5)
print()

arr6 = [random.randint(1,20) for i in range(10)]
print(arr6)
print()

arr7 = [[] for i in range(5)]
print(arr7)
print()

arr8 = [[1 for i in range(2)] for j in range(4)]
print(arr8)
print()

arr9 = [[random.randint(1,20) for i in range(3)] for j in range(5)]
print(arr9)
print()

#an array with values: 4,0,3
arr10 = [4, 0, 3]
print(arr10)
print()

#15-element array filled with zeros
arr11 = [0] * 15
print(arr11)
print()

#an array with integer values in the range of <1,30>
arr12 = [i for i in range(1,31)]
print(arr12)
print()

#20-element array filled with 0 or 1 randomly
arr13 = [random.randint(0,1) for i in range(20)]
print(arr13)
print()

#two dimensional array with five rows and two columns filled with False
arr14 = [[False for i in range(2)] for j in range(5)]
print(arr14)
print()