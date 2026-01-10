array = [[-38, 19], [5, 40], [-7, 11], [29, 16]]


min_val = array[0][0]
max_val = array[0][0]
min_pos = (0, 0)
max_pos = (0, 0)


for i in range(len(array)):
    for j in range(len(array[i])):
        value = array[i][j]
        if value < min_val:
            min_val = value
            min_pos = (i, j)
        if value > max_val:
            max_val = value
            max_pos = (i, j)


print(f"Smallest value: {min_val} at row {min_pos[0]}, column {min_pos[1]}")
print(f"Largest value: {max_val} at row {max_pos[0]}, column {max_pos[1]}")