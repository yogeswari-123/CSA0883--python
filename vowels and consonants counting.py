def count_vowels_consonants(text):
    vowels = "aeiou"
    num_vowels = 0
    num_consonants = 0
    
    for char in text.lower():
        if char.isalpha():
            if char in vowels:
                num_vowels += 1
            else:
                num_consonants += 1
    
    print("Number of vowels =", num_vowels)
    print("Number of consonants =", num_consonants)
    
    if num_vowels > num_consonants:
        print("Vowels are maximum")
    elif num_consonants > num_vowels:
        print("Consonants are maximum")
    else:
        print("Equal number of vowels and consonants")
text = "Saveetha School of Engineering"
count_vowels_consonants(text)
