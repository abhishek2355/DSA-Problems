"""
# Problem Statement: 
Given an array of size n, write a program to check if the given array is sorted in (ascending / Increasing / Non-decreasing) order or not. 
If the array is sorted then return True, Else return False.
Note: Two consecutive equal values are considered to be sorted.
"""

def check(nums):
    n = len(nums)
    count = 0

    for i in range(1, n):
        if nums[i-1] > nums[i]:
            count += 1
    if nums[n-1] > nums[0]:
            count += 1
    return count <= 1

nums = list(map(int, input().split()))
print(check(nums))

