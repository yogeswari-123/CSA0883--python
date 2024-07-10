def print_even_until_20(nums):
    found_20 = False
    for num in nums:
        if num == 20:
            found_20 = True
            break
        if num % 2 == 0:
            print(num, end=' ')

    if not found_20:
        print("\n20 not found in the list.")


numbers = [10, 5, 18, 20, 12, 7, 22, 16]
print("Even numbers before first occurrence of 20:")
print_even_until_20(numbers)
