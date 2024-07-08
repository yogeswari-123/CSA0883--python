def count_special_characters(s):
    special_characters = 0
    for char in s:
        if not char.isalnum() and not char.isspace():
            special_characters += 1
    return special_characters

statement = input("Enter the statement: ")
special_count = count_special_characters(statement)
print(f"Special Characters: {special_count}")
