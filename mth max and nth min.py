def find_mth_maximum_nth_minimum(arr, M, N):
    if M <= 0 or N <= 0 or M > len(arr) or N > len(arr):
        return "Invalid input: M or N is out of range."
    sorted_arr = sorted(arr)
    Mth_max = sorted_arr[-M]
    Nth_min = sorted_arr[N-1]
    sum_val = Mth_max + Nth_min
    diff_val = Mth_max - Nth_min
    product_val = Mth_max * Nth_min
    return Mth_max, Nth_min, sum_val, diff_val, product_val
array_elements = [14, 16, 87, 36, 25, 89, 34]
M = 1
N = 3
Mth_max, Nth_min, sum_val, diff_val, product_val = find_mth_maximum_nth_minimum(array_elements, M, N)
print("Sample Output:")
print(f"{M}st Maximum Number = {Mth_max}")
print(f"{N}rd Minimum Number = {Nth_min}")
print(f"Sum = {sum_val}")
print(f"Difference = {diff_val}")
print(f"Product = {product_val}")
test_cases = [
    ([16, 16, 16, 16, 16], 0, 1),
    ([0, 0, 0, 0], 1, 2),
    ([-12, -78, -35, -42, -85], 3, 3),
    ([15, 19, 34, 56, 12], 6, 3),
    ([85, 45, 65, 75, 95], 5, 7)
]
print("\nTest Cases Output:")
for i, (test_case, M, N) in enumerate(test_cases, 1):
    result = find_mth_maximum_nth_minimum(test_case, M, N)
    if isinstance(result, str):
        print(f"Test case {i}: {result}")
    else:
        Mth_max, Nth_min, sum_val, diff_val, product_val = result
        print(f"Test case {i}: {M}th Maximum Number = {Mth_max}, {N}th Minimum Number = {Nth_min}")
        print(f"Sum = {sum_val}")
        print(f"Difference = {diff_val}")
        print(f"Product = {product_val}")
