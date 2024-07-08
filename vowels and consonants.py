def count_vowels_and_consonants(s):
    vowels = 0
    consonants = 0
    for char in s:
        if char.isalpha():
            if char.lower() in 'aeiou':
                vowels += 1
            else:
                consonants += 1
    return vowels, consonants

statement = "Hello, how are you?"
vowels, consonants = count_vowels_and_consonants(statement)
print(f"Number of vowels: {vowels}")
print(f"Number of consonants: {consonants}")
