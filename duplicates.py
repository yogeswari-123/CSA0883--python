def find_duplicates(lst):
    return [item for item in set(lst) if lst.count(item) > 1]

lst = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
duplicates = find_duplicates(lst)
print(f"Duplicate elements: {duplicates}")
