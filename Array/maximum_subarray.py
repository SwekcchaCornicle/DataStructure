nums = [-2,1,-3,4,-1,2,1,-5,4]
max_sum = float('-inf')
current_sum = 0
start = 0
ans_start = 0
ans_end = 0
for i, num in enumerate(nums):
    if current_sum + num < num:
        current_sum = num
        start = i
    else:
        current_sum += num

    if current_sum > max_sum:
        max_sum = current_sum
        ans_start = start
        ans_end = i

print(max_sum, nums[ans_start:ans_end+1])
