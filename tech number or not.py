def is_tech_number(num):
    s = str(num)
    return len(s) % 2 == 0 and (int(s[:len(s)//2]) + int(s[len(s)//2:])) ** 2 == num

num = int(input("Enter a number: "))
print(f"{num} is {'a Tech' if is_tech_number(num) else 'not a Tech'} number.")
