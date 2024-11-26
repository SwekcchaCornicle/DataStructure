#TINME O(N*2N) SPACE O(N)
def power_set (nums):
    output = []
    def helper (nums,i,subset):
        if i == len(nums):
            if subset not in output:
                output.append(subset.copy())
            return
        helper(nums,i+1,subset)
        subset.append(nums[i])
        helper(nums,i+1,subset)
        subset.pop()
    helper(nums,0,[])
    return output
print(power_set([1,1,3]))