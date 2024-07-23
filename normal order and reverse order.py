def arrange_alphabetically(word):
    return ''.join(sorted(word))
def arrange_reverse_alphabetically(word):
    return ''.join(sorted(word, reverse=True))
word = input("Enter the word: ")
word = word.upper()
alphabetical_order = arrange_alphabetically(word)
reverse_order = arrange_reverse_alphabetically(word)
print("Alphabetical Order Normal:", alphabetical_order)
print("Alphabetical Order Reverse:", reverse_order)
