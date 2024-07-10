def perform_operations(a, b):
    print(f"Numbers: {a} and {b}")
    addition = a + b
    print(f"Addition: {addition}") 
    subtraction = a - b
    print(f"Subtraction: {subtraction}")
    multiplication = a * b
    print(f"Multiplication: {multiplication}")
    if b != 0:
        int_division = a // b
        print(f"Integer Division: {int_division}")
    else:
        print("Integer Division: Division by zero error")
    if b != 0:
        floor_division = a // b
        print(f"Floor Division: {floor_division}")
    else:
        print("Floor Division: Division by zero error")
    if b != 0:
        modulo = a % b
        print(f"Modulo Division: {modulo}")
    else:
        print("Modulo Division: Division by zero error")
int1, int2 = 10, 3
float1, float2 = 10.5, 3.2

print("Operations on Integers:")
perform_operations(int1, int2)

print("\nOperations on Floats:")
perform_operations(float1, float2)
