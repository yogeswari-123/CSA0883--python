def remove_vowels(s):
    vowels = "aeiouAEIOU"
    without_vowels = ""
    for char in s:
        if char not in vowels:
            without_vowels += char
    return without_vowels

user_input = input("Enter a string: ")
result = remove_vowels(user_input)
print("String without vowels:", result)
