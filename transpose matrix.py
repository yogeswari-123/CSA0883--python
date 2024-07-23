def transpose_matrix(matrix):
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]

matrix = [
    [4, 6, 7, 8],
    [3, 7, 2, 7],
    [7, 3, 7, 5]
]

transposed_matrix = transpose_matrix(matrix)


for row in transposed_matrix:
    print(row)

