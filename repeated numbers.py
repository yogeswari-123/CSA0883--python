def find_duplicate(nums):
    
    slow = nums[0]
    fast = nums[0]
    
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    
    return slow


nums = [1, 3, 4, 2, 2]
print(find_duplicate(nums))  

nums = [3, 1, 3, 4, 2]
print(find_duplicate(nums)) 

nums = [1, 1]
print(find_duplicate(nums)) 

nums = [1, 2, 2, 3, 4]
print(find_duplicate(nums))  
