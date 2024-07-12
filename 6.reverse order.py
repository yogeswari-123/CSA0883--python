def arrange_letters(word):
    # Sort the letters alphabetically
    normal_order = ''.join(sorted(word))
    
    # Sort the letters in reverse alphabetical order
    reverse_order = ''.join(sorted(word, reverse=True))
    
    return normal_order, reverse_order

# Example usage:
word = input("Enter the word: ").upper()  # Convert input to uppercase for consistency

normal, reverse = arrange_letters(word)

print(f"Normal order: {normal}")
print(f"Alphabetical Order Reverse: {reverse}")
