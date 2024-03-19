# Problem Statement: Given a number N reverse the number and print it.

def reverse(n):
    ans = 0
    while n:
        r = n % 10
        ans = ans * 10 + r
        n = n // 10
    return ans


n = int(input())
print(reverse(n))