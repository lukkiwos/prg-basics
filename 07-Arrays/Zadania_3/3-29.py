def create_2d_arr(x,y):
    array_2d = []

    for i in range(x):
        row = [0] * y
        array_2d.append(row)

    return array_2d


arr = create_2d_arr(3,5)

for row in arr:
    print(row)