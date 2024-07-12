def count_letters_digits(input_string):
    letters = 0
    digits = 0

    for char in input_string:
        if char.isalpha():
            letters += 1
        elif char.isdigit():
            digits += 1
    
    return letters, digits

input_string = "Python 3.2"
letter_count, digit_count = count_letters_digits(input_string)

print("Input String:", input_string)
print("Letters:", letter_count)
print("Digits:", digit_count)
