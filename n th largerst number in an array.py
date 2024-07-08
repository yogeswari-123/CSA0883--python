def find_nth_largest(nums, n):
    nums_sorted = sorted(set(nums), reverse=True)
    if n <= len(nums_sorted):
        return nums_sorted[n - 1]
    else:
        return None


numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
n = 3
nth_largest = find_nth_largest(numbers, n)
if nth_largest is not None:
    print(f"The {n}th largest number is: {nth_largest}")
else:
    print(f"There is no {n}th largest number in the list.")
