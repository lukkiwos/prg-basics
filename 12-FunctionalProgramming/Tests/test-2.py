arr = [2,3,4,5]

iloczyn = lambda x: x*2

# for i in arr:
    # print( iloczyn(i) )


map(iloczyn,arr)               # map(funckja,dane)

print(list(map(iloczyn,arr)))


# print( list(map(lambda x: x*2, arr)) )