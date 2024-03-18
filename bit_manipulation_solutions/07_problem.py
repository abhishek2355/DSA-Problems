# Problem Link: https://leetcode.com/problems/single-number-iii/description/

# Solution 1: Using dict.
from collections import Counter 
def ans(nums):
    test = Counter(nums)
    test_sort = sorted(test.items(), key = lambda x: x[1])
    count = 0
    ans = []
    for i, j in test_sort:
        ans.append(i)
        if(count == 1):
            break
        count += 1
    return ans

# Solution 2: Using bit manipulation.
def ans2(nums):
    xor = 0
    for i in nums:
        xor = (xor ^ i)
    right_most = (xor & xor-1) ^ xor
    b1 = 0
    b2 = 0
    for i in nums:
        if i & right_most:
            b1 = b1 ^ i
        else:
            b2 = b2 ^ i
    return [b1, b2]

nums = [1,2,1,3,2,5]
print(ans(nums))
print(ans2(nums))