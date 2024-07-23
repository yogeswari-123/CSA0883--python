def removeKdigits(num, k):
    stack = []
    for digit in num:
        while k > 0 and stack and stack[-1] > digit:
            stack.pop()
            k -= 1
        stack.append(digit)
    
   
    final_stack = stack[:-k] if k else stack
   
    result = ''.join(final_stack).lstrip('0')
    
    return result or '0'


num = "1432219"
k = 3
print(removeKdigits(num, k)) 

num = "10200"
k = 1
print(removeKdigits(num, k))  

num = "10"
k = 2
print(removeKdigits(num, k))  
