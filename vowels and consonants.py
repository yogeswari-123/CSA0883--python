def count_vowels_and_consonants(statement):
    vowels = "aeiouAEIOU"
    num_vowels = 0
    num_consonants = 0
    
    for char in statement:
        if char.isalpha():  
            if char in vowels:
                num_vowels += 1
            else:
                num_consonants += 1
    
    return num_vowels, num_consonants

def main():
    statement = "Saveetha School of Engineering"
    num_vowels, num_consonants = count_vowels_and_consonants(statement)
    
    print(f"Number of vowels = {num_vowels}")
    print(f"Number of consonants = {num_consonants}")
    
    if num_vowels > num_consonants:
        print("Vowels are more.")
    elif num_consonants > num_vowels:
        print("Consonants are more.")
    else:
        print("Number of vowels and consonants are equal.")

if __name__ == "__main__":
    main()
