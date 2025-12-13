matrix = [
   [0,0,0],
   [0,0,0],
   [0,0,0]
]


n = len(matrix)

for i in range(n):
    matrix[i][i] = 1

print()

for row in matrix:
    print(' '.join(map(str, row)))