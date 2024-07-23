def calculate_difference(N):
    sum_of_squares = sum(i**2 for i in range(1, N+1))
    square_of_sum = sum(range(1, N+1)) ** 2
    difference = square_of_sum - sum_of_squares
    return difference
N = 5
difference = calculate_difference(N)
print(f"Diff={difference}")
