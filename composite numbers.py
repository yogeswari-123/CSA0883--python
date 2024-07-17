def is_composite(num):
    if num < 4:
        return False
    for i in range(2, num):
        if num % i == 0:
            return True
    return False
def count_composite_numbers(arr):
    count = 0
    for num in arr:
        if is_composite(num):
            count += 1
    return count
arr1 = [16, 18, 27, 16, 23, 21, 19]
arr2 = [26, 28, 37, 26, 33, 31, 29]
arr3 = [1.6, 1.8, 2.7, 1.6, 2.3, 2.1, 19]
arr4 = [0, 160, 180, 270, 160, 230, 210, 190, 0]
arr5 = [200, 180, 180, 270, 270, 270, 190, 200]
arr6 = [100, 100, 100, 100, 100, 100, 100, 100]
print("Number of Composite Numbers in arr1:", count_composite_numbers(arr1))
print("Number of Composite Numbers in arr2:", count_composite_numbers(arr2))
print("Number of Composite Numbers in arr3:", count_composite_numbers(arr3))
print("Number of Composite Numbers in arr4:", count_composite_numbers(arr4))
print("Number of Composite Numbers in arr5:", count_composite_numbers(arr5))
print("Number of Composite Numbers in arr6:", count_composite_numbers(arr6))
