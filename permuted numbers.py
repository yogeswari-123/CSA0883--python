def permute_unique(nums):
    def backtrack(start):
        if start == len(nums):
            permutations.add(tuple(nums[:]))
            return
        for i in range(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start]
            backtrack(start + 1)
            nums[start], nums[i] = nums[i], nums[start]

    permutations = set()
    backtrack(0)
    return [list(p) for p in permutations]


nums = [1, 1, 2]
output = permute_unique(nums)
print(output)  
