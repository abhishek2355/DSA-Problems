# Problem Link: https://leetcode.com/problems/single-number/description/

# Using HashMap. Time complexity is (n*log(n) + m ) where m = n/2 = len(dict)
from collections import Counter
def single_number(nums):
    test = Counter(nums)
    temp = sorted(test.items(), key= lambda item: item[1])
    for i,j in temp:
        return i

# O(n) time complexity
def bits(nums):
    xor = 0
    for i in nums:
        xor = xor ^ i
    return xor

nums = [4,1,2,1,2]
print(single_number(nums))
print(bits(nums))