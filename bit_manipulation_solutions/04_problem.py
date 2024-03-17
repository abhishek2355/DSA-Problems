# Check the given number is pow of 2 or not.
# https://leetcode.com/problems/power-of-two/

# Best way is the 

def ans(n):
    if n != 0:
        if(n & n-1 == 0):
            return True
        else:
            return False
    else:
        return False
    
    
n = int(input())
print(ans(n))

