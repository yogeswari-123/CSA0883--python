def sumsquare(l):
    odd_sum = sum(x ** 2 for x in l if x % 2 != 0)
    even_sum = sum(x ** 2 for x in l if x % 2 == 0)
    return [odd_sum, even_sum]

def read_and_process():
    n = int(input("Enter the number of elements: "))
    elements = []
    for _ in range(n):
        elements.append(int(input("Enter the element: ")))
    result = sumsquare(elements)
    print("Output:")
    print(result)

read_and_process()
