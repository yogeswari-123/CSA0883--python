def calculate_averages():
    positive_sum = 0
    negative_sum = 0
    positive_count = 0
    negative_count = 0
    while True:
        num = float(input("Enter the number: "))
        if num == -1:
            break
        elif num > 0:
            positive_sum += num
            positive_count += 1
        elif num < 0:
            negative_sum += num
            negative_count += 1
    if positive_count > 0:
        positive_avg = positive_sum / positive_count
    else:
        positive_avg = 0

    if negative_count > 0:
        negative_avg = negative_sum / negative_count
    else:
        negative_avg = 0
    print(f"The average of negative numbers is: {negative_avg:.2f}")
    print(f"The average of positive numbers is: {positive_avg:.2f}")
print("Enter -1 to exit…")
calculate_averages()
print("\nTest case outputs:")
test_inputs = [
    [-1, 43, -87, -29, 1, -9, -1],
    [73, -76, 2, 10, 28, -1],
    [-5, -9, -46, 2, 5, 0, -1],
    [9, 11, -5, 6, 0, -1],
    [-1, -1, -1, -1, -1]
]
def run_test_cases(test_inputs):
    import io
    import sys
    for test_case in test_inputs:
        input_stream = io.StringIO('\n'.join(map(str, test_case)) + '\n')
        sys.stdin = input_stream
        print(f"\nRunning test case: {test_case}")
        calculate_averages()
run_test_cases(test_inputs)
