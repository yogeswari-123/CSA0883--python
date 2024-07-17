def count_negative_numbers(elements):
    count = 0
    for num in elements:
        if num < 0:
            count += 1
    return count

sample_elements = [16, -18, 27, -16, 23, -21, 19]
print("Sample Output:")
print(f"Number of negative numbers in List of elements = {count_negative_numbers(sample_elements)}")


test_cases = [
    [-26, 28, 37, -26, 33, -31, -29],
    [1.6, 1.8, 2.7, -1.6, 2.3, -2.1, 0.19],
    [0, 160, 180, 270, 160, 230, 210, 190, 0],
    [-16, 2.8, -7, -1.5, 2.8, -2.8, -0.19],
    [-160, -160, -180, -270, -160, -230, -210, -190, 0]
]

print("Test Cases Output:")
for i, test_case in enumerate(test_cases, 1):
    print(f"Test case {i}: Number of negative numbers in List of elements = {count_negative_numbers(test_case)}")
