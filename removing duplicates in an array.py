def remove_duplicates(arr):
    if not arr:
        return []
    
    unique_elements = [arr[0]]
    for num in arr[1:]:
        if num != unique_elements[-1]:
            unique_elements.append(num)
    
    return unique_elements


sorted_array = [1, 2, 2, 3, 4, 4, 4, 5, 6, 6]
result = remove_duplicates(sorted_array)
print("Sorted Array with Duplicates Removed:", result)
