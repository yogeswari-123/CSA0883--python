def gcd(a, b): return gcd(b, a % b) if b else a
def lcm(a, b): return a * b // gcd(a, b)
num1, num2 = int(input("Enter the first number: ")),   int(input("Enter the second number: "))
print(f"The GCD of {num1} and {num2} is: {gcd(num1, num2)}")
print(f"The LCM of {num1} and {num2} is: {lcm(num1, num2)}")
