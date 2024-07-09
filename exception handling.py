def divide_numbers(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except TypeError:
        print("Error: Invalid input type. Both inputs must be numbers.")

print(divide_numbers(10, 2))    
print(divide_numbers(10, 0))    
print(divide_numbers(10, '7'))  
