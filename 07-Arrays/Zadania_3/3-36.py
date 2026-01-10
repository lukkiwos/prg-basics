def flatten_matrix(matrix):
    flat = []
    for row in matrix:
        for value in row:
            flat.append(value)
    return flat



def print_array(arr):
    print(" ".join(map(str, arr)))



matrices = [
    [
        [2, 3],
        [1, 5]
    ],
    [
        [5, 0, 3, 7, 5],
        [9, 0, 9, 1, 2]
    ],
    [
        [2, 1],
        [3, 5],
        [7, 4],
        [2, 6]
    ]
]

for m in matrices:
    print("Original 2D array:")
    for row in m:
        print(" ".join(map(str, row)))
    flat = flatten_matrix(m)
    print()
    print("Flattened 1D array:")
    print_array(flat)
    print()  
