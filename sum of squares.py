def sum_of_squares(N):
    return sum(i**2 for i in range(1, N + 1))


N = 6

result = sum_of_squares(N)

print(f"Sum = {result}")

