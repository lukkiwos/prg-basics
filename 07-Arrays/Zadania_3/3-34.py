def identity_matrix(n):
    # Tworzymy pustą tablicę 2D
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            if i == j:
                row.append(1)
            else:
                row.append(0)
        matrix.append(row)
    return matrix


def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))



sizes = [3, 5, 8]

for n in sizes:
    print(f"Identity matrix {n}x{n}:")
    mat = identity_matrix(n)
    print_matrix(mat)
    print()
