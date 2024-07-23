def check_mirror_number(number):
    # Reverse the number
    reversed_number = number[::-1]
    print(f"Mirror image: {reversed_number}")
    if number == reversed_number:
        print("The number is a mirror number.")
    else:
        print("The number is not a mirror number.")
number = input("Enter the number: ")
check_mirror_number(number)
