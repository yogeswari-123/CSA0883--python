def is_substring(sub, string):
    return sub in string

sub = input("Enter the substring: ")
string = input("Enter the main string: ")
print(f"'{sub}' is {'a substring' if is_substring(sub, string) else 'not a substring'} of '{string}'.")
