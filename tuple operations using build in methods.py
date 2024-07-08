my_tuple = (1, 2, 3, 4, 5)
print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])
print("Slicing tuple:", my_tuple[2:4])
print("Length of tuple:", len(my_tuple))
tuple1 = (1, 2, 3)
tuple2 = ('a', 'b', 'c')
concatenated_tuple = tuple1 + tuple2
print("Concatenated tuple:", concatenated_tuple)
repeated_tuple = tuple1 * 3
print("Repeated tuple:", repeated_tuple)
print("Is 3 in tuple?", 3 in my_tuple)
print("Iterating through tuple:")
for item in my_tuple:
    print(item)
print("Index of element 4:", my_tuple.index(4))
print("Count of element 3:", my_tuple.count(3))
a, b, c, d, e = my_tuple
print("Unpacked variables:", a, b, c, d, e)
