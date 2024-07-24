def is_perfect(num):
    return num == sum(i for i in range(1, num) if num % i == 0)

num = int(input("Enter a number: "))
print(f"{num} is {'a perfect' if is_perfect(num) else 'not a perfect'} number.")
