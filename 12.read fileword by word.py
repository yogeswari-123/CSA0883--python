def read_file_words(filename):
    try:
        with open(filename, 'r') as file:
            words = file.read().split()
            return words
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return []

filename = 'sample.txt'  

words = read_file_words(filename)
if words:
    print("Words in the file:")
    for word in words:
        print(word)
