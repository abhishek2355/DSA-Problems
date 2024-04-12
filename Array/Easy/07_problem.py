"""
# problem Url: https://leetcode.com/problems/move-zeroes/description/
"""
def ans(nums):
    i = 0
    j = 0
    if len(nums) == 1:
        return nums
    while i < len(nums) and j < len(nums):
        if nums[i] != 0 and i < len(nums):
            i += 1
            continue
        if i > j or nums[j] == 0:
            if j < len(nums):
                j += 1
                continue
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
        i += 1
        j += 1
    return nums

nums = list(map(int, input().split()))
print(ans(nums))