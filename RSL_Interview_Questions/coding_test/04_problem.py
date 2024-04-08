"""
# Problem Stetment:
Given two strings ‘s’ = “abc” and ‘t’ = “pqr”, return true if ‘s’ is a subsequence of ‘t’, or false otherwise.
A subsequence of a string is a new string that is formed from the original string by deleting some (can be
none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is
a subsequence of "abcde" while "aec" is not).

# Examples:
1. Input: s = "abc", t = "ahbgdc"
   Output: true
2. Input: s = "axc", t = "ahbgdc"
   Output: false
3. Input: s = "agb", t = "ahbgdc"
   Output: fals
"""

def issubsequence(s, t):
    j = 0
    for i in t:
        if j < len(s) and s[j] == i:
            j += 1
    return j == len(s)

s = input('Enter the first string: ')
t = input('Enter the second string: ')
print(issubsequence(s, t))
