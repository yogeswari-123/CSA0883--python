
tuple1 = (4, 7, 1, 8, 3, 9)
tuple2 = (6, 2, 5, 3, 7, 1)

max_tuple1 = max(tuple1)
min_tuple1 = min(tuple1)

print(f"Tuple1: {tuple1}")
print(f"Maximum of tuple1: {max_tuple1}")
print(f"Minimum of tuple1: {min_tuple1}")


sum_of_tuples = tuple(map(sum, zip(tuple1, tuple2)))

print(f"Tuple2: {tuple2}")
print(f"Sum of tuple1 and tuple2: {sum_of_tuples}")


duplicate_tuple1 = tuple1 * 2

print(f"Duplicate of tuple1: {duplicate_tuple1}")


slice_tuple1 = tuple1[1:4]

print(f"Slicing tuple1 from index 1 to 3: {slice_tuple1}")


list_from_tuple1 = list(tuple1)

print(f"List obtained from tuple1: {list_from_tuple1}")
