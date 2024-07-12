word = input("Enter the word: ").upper()
repeated_letters = {letter for letter in word if word.count(letter) > 1}

num_repeated = len(repeated_letters)
print(f"Number of repeated letters = {num_repeated}")
if num_repeated > 0:
    print(f"Repeated letter(s) = {' '.join(repeated_letters)}")
