def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
def find_non_composite(numbers):
    non_composite_numbers = []
    for num in numbers:
        if is_prime(num):
            non_composite_numbers.append(num)
    return non_composite_numbers
test_cases = [
    [26, 28, 37, 26, 33, 31, 29],
    [1.6, 1.8, 2.7, 1.6, 2.3, 2.1, 19],
    [0, 160, 180, 270, 160, 230, 210, 190, 0],
    [20, 18, 18, 27, 27, 27, 190, 20],
    [100, 100, 100, 100, 100, 100, 100, 100]
]

for i, test_case in enumerate(test_cases):
    non_composite_numbers = find_non_composite(test_case)
    print(f"Test case {i + 1}:")
    print(f"Array of elements = {test_case}")
    print(f"Prime numbers in Array elements = {non_composite_numbers}")
    print()
