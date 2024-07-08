my_dict = {
    'name': 'vyshu',
    'age': 20,
    'city': 'chennai'
}
print("Items in dictionary:")
for key, value in my_dict.items():
    print(f"{key}: {value}")
print("\nKeys in dictionary:")
for key in my_dict.keys():
    print(key)
copied_dict = my_dict.copy()
print("\nCopied dictionary:")
for key, value in copied_dict.items():
    print(f"{key}: {value}")
