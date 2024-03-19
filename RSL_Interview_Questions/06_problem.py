# find unique element in array using O(n) time and O(1) space complexity.
# The best solution is using XOR. We can also slove it using dict in python, or map in c++.
# Same question is in bit manipulation folder.

def solution(arr):
    xor = 0
    for i in arr:
        xor = xor ^ i
    return xor

test = [2, 3, 5, 4, 5, 3, 4]
print(solution(test))