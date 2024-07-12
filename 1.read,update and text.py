def write_to_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)
    print(f"Written to {filename}")

def read_from_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
        print(f"Content of {filename}:")
        print(content)
    except FileNotFoundError:
        print(f"{filename} not found.")

def update_file(filename, new_content):
    try:
        with open(filename, 'a') as file:
            file.write(new_content)
        print(f"Updated {filename}")
    except FileNotFoundError:
        print(f"{filename} not found.")
filename = 'example.txt'

write_to_file(filename, "This is the original content.\n")


read_from_file(filename)


update_file(filename, "This is the appended content.\n")

read_from_file(filename)
 
