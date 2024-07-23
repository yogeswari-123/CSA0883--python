def removeKdigits(num, k):
    stack = []
    for digit in num:
        while k > 0 and stack and stack[-1] > digit:
            stack.pop()
            k -= 1
        stack.append(digit)
    
  
    while k > 0:
        stack.pop()
        k -= 1
    
    
    result = ''.join(stack).lstrip('0')
    
 
    return result if result else "0"


num = "1432219"
k = 3
print(f"Smallest possible integer after removing {k} digits from {num} is {removeKdigits(num, k)}")
