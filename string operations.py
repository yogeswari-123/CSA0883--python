string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
concatenated = string1 + string2
reversed_string1, reversed_string2 = string1[::-1], string2[::-1]
slice_start, slice_end = int(input("Start index: ")), int(input("End index: "))
print(f"Concatenated: {concatenated}\nReversed 1st: {reversed_string1}\nReversed 2nd: {reversed_string2}\nSliced: {string1[slice_start:slice_end]}\nLength 1st: {len(string1)}\nLength 2nd: {len(string2)}")
