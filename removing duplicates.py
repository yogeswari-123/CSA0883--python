def remove_duplicates(arr):
    if not arr:
        return []
    unique_arr = [arr[0]]
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            unique_arr.append(arr[i])
    return unique_arr
arr1 = [16, 16, 16, 16, 16]
arr2 = [0, 0, 0, 0]
arr3 = [-12, -78, -35, -42]
arr4 = [1, 2, 3, 7, 8, 9, 4, 5, 6]
arr5 = [1, 2, 3, 4, 5, 6]
print(remove_duplicates(arr1)) 
print(remove_duplicates(arr2)) 
print(remove_duplicates(arr3))  
print(remove_duplicates(arr4))  
print(remove_duplicates(arr5))
