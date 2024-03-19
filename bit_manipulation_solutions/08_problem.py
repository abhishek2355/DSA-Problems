# Problem: Given an int number n. Find the XOR in range (1-n).

# brute force approch  // Time complexity O(n)
def bruteForceApproch(n: int):
    ans = 0 
    for i in range(1, n+1):
        ans = ans ^ i
    return ans

# Optimal Solution
# If we check the pattern.
# n = 1 --> 1
# n = 2 --> 3
# n = 3 --> 0
# n = 4 --> 4 
# This pattern will as it's for the every 4 numbers
def optimalSolution(n: int):
    if n % 4 == 1:
        return 1
    elif n % 4 == 2:
        return n+1
    elif n % 4 == 3:
        return 0
    else:
        return n
    
n = int(input())
print(bruteForceApproch(n))
print(optimalSolution(n))


# If the question like find the XOR between L to R. 
# The optimal solution will be xor of (1 to L) ^ xor of (1 to R).