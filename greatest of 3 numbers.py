def find_greatest(a, b, c):
    if a > b:
        if a > c:
            return a
        else:
            return c
    else:
        if b > c:
            return b
        else:
            return c

# Example usage
a = 5
b = 10
c = 3
greatest = find_greatest(a, b, c)
print(f"The greatest number among {a}, {b}, and {c} is {greatest}.")
