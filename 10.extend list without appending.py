def extend_list(list1, list2):
    list2.extend(list1)
    return list2


list1 = [10, 20, 30]
list2 = [40, 50, 60]


extended_list = extend_list(list1, list2)


print("Expected Output:", extended_list)
