"""
Problem Stetment: 
Write a program to find the equilibrium element from an integer array. An equilibrium element is
defined as the number for which the sum of left side elements is equal to sum of right side elements.

Note: If no possible combination exists return 0.

Examples:
 1. Input: [1,7, 5, 2, 6]
    Output: 5 (since 1 + 7 = 8 and 2 + 6 = 8)
 2. Input: [10, 1, 1, 9]
    Output: 1 (since 1 + 9 = 10 and first element is 10)
Below is the code in python.
"""

def equilibrium(nums):
    total_sum = 0
    left_sum = 0

    for i in nums:
        total_sum += i

    for i in nums:
        total_sum -= i
        if(left_sum == total_sum):
            return i
        else:
            left_sum += i

    return 0

nums = list(map(int, input('Enter the list of elements: ').split()))
print('Equilibrium element is: ', equilibrium(nums))
