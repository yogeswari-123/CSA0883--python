def count_words(text):
    return len(text.split())

text = input("Enter a string: ")
print(f"The number of words in the string is: {count_words(text)}")
