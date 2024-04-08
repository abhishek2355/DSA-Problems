"""
# Problem Stetment:
Given an string as an input. Revese the words in that string.

# Test Case:
    1. input: I like programming
       output: programming like I
"""
# Using In-Built Function.
def approach_1(s):
    ans = ''
    temp = s.split(" ")
    test = temp[::-1]

    for i in test:
        ans += i
        ans += " "
    return ans

def approach_2(s):
    temp_str = ''
    final_str = ''
    for i in s:
        if i == " ":
            final_str = temp_str + " " + final_str
            temp_str = ''
        else:
            temp_str += i
    final_str = temp_str + " " + final_str
    return final_str



s = input('Enter the string: ')
print(approach_1(s))
print(approach_2(s))
