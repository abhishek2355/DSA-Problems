"""
# Problem Stetment:
Given an integer number n. Your task is the sum of all the digits till the resulting sum not a single integer.

# Test Case:
    1. input: 5678
       output: (26) --> (8)
"""
def ans(n):
    final = 0
    while n or final > 9:
        if n == 0:
            n = final
            final = 0
        final += n % 10
        n = n // 10
    return final


n = int(input('Enter the number: '))
print('Sum of digits in single digit is: ', ans(n))