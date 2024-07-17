def create_tuple_list(lower_range, upper_range):
    tuple_list = []
    for i in range(lower_range, upper_range+1):
        tuple_list.append((i, i*i))
    return tuple_list
lower_range = int(input("Enter the lower range: "))
upper_range = int(input("Enter the upper range: "))
if upper_range < lower_range:
    print("Upper range should be greater than lower range. Please try again.")
else:
    result = create_tuple_list(lower_range, upper_range)
    print(result)
