nums = [2,7,11,15], target = 9
def twoSum(nums, target):
        has_map = {}
        for i, v in enumerate(nums):
            number = target - v
            if number in has_map:
                return [i , has_map[number]]
            has_map[v] = i