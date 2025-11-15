def containsDuplicate(nums):
    hash_map = []
    for i in nums:
        print(i)
        if i in hash_map:
            return True
        hash_map.append(i)
        print(hash_map)
        return False
print(containsDuplicate([1,2,3,1]))

# or decrease time

def containsDuplicate(nums):
    x = set(nums)
    if len(x) ==  len(nums):
        return False
    return True
print(containsDuplicate([1,2,3,1]))