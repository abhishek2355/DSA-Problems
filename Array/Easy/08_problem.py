"""
#Problem Stetment:
Given an array nums containing n distinct numbers in the range [0, n], 
return the only number in the range that is missing from the array.

# Problem URL: https://leetcode.com/problems/missing-number/description/
"""

def ans(nums):
    n = len(nums)
    total_sum = (n*(n+1))//2
    test = sum(nums)
    return total_sum - test

nums = list(map(int, input().split()))
print(ans(nums))