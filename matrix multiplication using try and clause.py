def matrix_multiply(A, B):
    try:
        if len(A[0]) != len(B):
            raise ValueError("Number of columns in A must be equal to number of rows in B")
        
        result = [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
        return result
    except Exception as e:
        print(f"An error occurred: {e}")
A = [
    [1, 2, 3],
    [4, 5, 6]
]
B = [
    [7, 8],
    [9, 10],
    [11, 12]
]
result = matrix_multiply(A, B)
if result:
    print("Result of matrix multiplication:")
    for row in result:
        print(row)
