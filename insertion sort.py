def insertion_sort(arr):
    n = len(arr)
    
    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key
    
    return arr


arr = [12,98,67,35,75,85]
print("Original array:", arr)
sorted_arr = insertion_sort(arr)
print("Sorted array:", sorted_arr)
