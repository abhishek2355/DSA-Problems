"""
Rotate array by K elements

# Problem Statement: 
Given an array of integers, rotating array of elements by k elements either left or right.

# Examples:

Example 1:
Input: N = 7, array[] = {1,2,3,4,5,6,7} , k=2 , right
Output: 6 7 1 2 3 4 5
Explanation: array is rotated to right by 2 position .

Example 2:
Input: N = 6, array[] = {3,7,8,9,10,11} , k=3 , left 
Output: 9 10 11 3 7 8
Explanation: Array is rotated to right by 3 position.

"""
# Method for reverse the array.
def reverse_arr(nums, i , j):
    while i < j:
        temp  = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
        i += 1
        j -= 1
    
def rotate_by_k(nums, k):
    # First reverse the whole array.
    reverse_arr(nums, 0, len(nums) - 1)
    # Reverse the first k part of the arr. 
    reverse_arr(nums, 0, k - 1)
    # Reverse the remaining part of the arr. 
    reverse_arr(nums, k, len(nums) -1)

    return nums

nums = list(map(int, input().split()))
k = int(input())
print(rotate_by_k(nums, k))