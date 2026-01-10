array = [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0]
] 


for i in range(5):
    for j in range(5):
        array[i][j] = (i+1) * (j+1)


for row in array:
    for value in row:
        print(f"{value:2}", end=" ")
    print()