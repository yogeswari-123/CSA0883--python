def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

num = int(input("Enter a number: "))
print(f"{num} is {'a prime' if is_prime(num) else 'not a prime'} number.")
