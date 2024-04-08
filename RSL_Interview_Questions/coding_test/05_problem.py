"""
# Problem Stetment:
Given a string ‘s’ consisting only of characters 'a', 'b', and 'c'. You are asked to apply the following
algorithm on the string any number of times:
    1. Pick a non-empty prefix from the string ‘s’ where all the characters in the prefix are the same.
    2. Pick a non-empty suffix from the string ‘s’ where all the characters in this suffix are the same.
    3. The prefix and the suffix should not intersect at any index.
    4. The characters from the prefix and suffix must be the same.
    5. Delete both the prefix and the suffix.
    6. Return the minimum length of ‘s’ after performing the above operation any number of times (possibly
        zero times).

# Examples:
1. Input: s = "ca"
Output: 2
Explanation: You can't remove any characters, so the string stays as is.
2. Input: s = "aabccabba"
Output: 3
Explanation: An optimal sequence of operations is:- Take prefix = "aa" and suffix = "a" and remove them, s = "bccabb".- Take prefix = "b" and suffix = "bb" and remove them, s = "cca
"""

def ans(s):
    left = 0
    right = len(s)-1
    while left < right and s[left] == s[right]:
        char = s[left]
        while left < right and s[left] == char:
            left  += 1
        while left < right and s[right] == char:
            right -= 1
            
    return right - left + 1
        
s = input('Enter the string: ')
print('Minimum length of String: ', ans(s))
