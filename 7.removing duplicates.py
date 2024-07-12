def remove_duplicates(lst):
    return list(set(lst))


my_list = [1, 2, 3, 3, 4, 5, 5, 6]
unique_list = remove_duplicates(my_list)
print("Original List:", my_list)
print("List with Duplicates Removed:", unique_list)
