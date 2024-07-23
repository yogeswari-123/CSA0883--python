def linear_search(lst, target):
    for element in lst:
        if element == target:
            return "Exist"
    return "Not exist"


lst = [2, 4, 6, 8, 9, 7, 9]


target1 = 7
result1 = linear_search(lst, target1)
print(f"Target: {target1}\nResult: {result1}")

target2 = 5
result2 = linear_search(lst, target2)
print(f"Target: {target2}\nResult: {result2}")

