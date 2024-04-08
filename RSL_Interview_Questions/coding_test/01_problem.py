""" 
Problem Stetment: 
Given a binary string (string containing only 0’s and 1’s) “str” that contains at least a single
occurrence of a numeric value: '1'.
You have to rearrange the characters in the string in such a way that the resulting binary string is the
maximum odd binary number that can be created from this combination.
Note that the resulting string can have leading zeros.

Examples:
 1. Input: str = "010"
    Output: "001"
 2. Input: str = "01010"
    Output: "10001"

Approach: 
First count the number of 1's in the string. Then add the 1's at the start of new string and keep one (1)
and insert it into the ending of the new string. Below is the code.
"""

def max_number(s):
    ans = ''
    one = 0
    for i in s:
        if i == '1':
            one += 1
    for i in range(one-1):
        ans += '1'

    for i in range(one-1, len(s)-1):
        ans += '0'
    ans += '1'
    return ans

s = input("Enter the string: ")
print("Maximum odd number is: ", max_number(s))

