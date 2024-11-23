#Given numbers, nums dulicates return all possible parameter array space o(n) time 0(n!*n)
def permute(nums):
    def backtrack(start):
        if start == len(nums):
            if nums not in res:
                res.append(nums[:])
            
        for i in range(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start]  # First swap
            backtrack(start + 1)
            nums[start], nums[i] = nums[i], nums[start]  # Second swap
    res = []
    backtrack(0)
    return res

# List of numbers
numbers = [1, 1, 3]

# Generate permutations
permutations = permute(numbers)
print(permutations)