
def swap_with_temp(a, b):
    print(f"Before swapping: a = {a}, b = {b}")
    
    temp = a
    a = b
    b = temp
    
    print(f"After swapping: a = {a}, b = {b}")


x = 5
y = 10
swap_with_temp(x, y)
