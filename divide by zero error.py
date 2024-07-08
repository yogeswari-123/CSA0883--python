try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    result = numerator / denominator
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
else:
    print(f"The result of {numerator} / {denominator} is {result}")
finally:
    print("Execution complete.")
