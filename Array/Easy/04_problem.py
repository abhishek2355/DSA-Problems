"""
#Problem Statement: 
Given an integer array sorted in non-decreasing order, remove the duplicates in place such that each unique element appears only once. The relative order of the elements should be kept the same.
If there are k elements after removing the duplicates, then the first k elements of the array should hold the final result. It does not matter what you leave beyond the first k elements.

Note: Return k after placing the final result in the first k slots of the array.
"""
# Using inbuild method.
def removeDuplicates_approch1(nums):
    test = set(nums)
    nums.clear()
    for i in test:
        nums.append(i)
    nums.sort()
    return nums

# Using 2 pointer.
def removeDuplicates_approch2(nums):
    i = 0
    for j in range(1, len(nums)):
        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]
    return nums[0: i + 1]
            

nums = list(map(int, input().split()))
print(removeDuplicates_approch1(nums))
print(removeDuplicates_approch2(nums))