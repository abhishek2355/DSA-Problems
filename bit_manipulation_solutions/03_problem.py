# Problem: Remove the right most set bit 
# if 10100 --> 10000
# Let n = 20 (10100)
# we know 19 (10011)
# After take & (10000)

n = int(input())
ans = n & n-1
print(ans)