def find_character(string, char):
    found = False
    for index in range(len(string)):
        if string[index] == char:
            print(f"{char} is found in string at index: {index}")
            found = True
            break
    if not found:
        print(f"{char} is not found in the string")


string = input("Enter the string: ")
char = input("Enter the character to be searched: ")


find_character(string, char)
