def is_tech_number(number):
    return number % sum(int(digit) for digit in str(number)) == 0


num = int(input("Enter a number: "))

if is_tech_number(num):
    print(f"{num} is a Tech number.")
else:
    print(f"{num} is not a Tech number.")
