def is_armstrong(num):
    num_str = str(num)
    num_digits = len(num_str)
    return num == sum(int(digit) ** num_digits for digit in num_str)

num = int(input("Enter a number: "))
print(f"{num} is {'an Armstrong' if is_armstrong(num) else 'not an Armstrong'} number.")
