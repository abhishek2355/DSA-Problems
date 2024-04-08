"""
# Problem Stetment:
Given an r as a rupees. If you go to shop, you can buy 1 chocolate for 1 rupees. After that if we return 3
empty packet we get one new chocolate. What will be the maximum chocolate that can we buy with the given rupees r.

# Test case: 
    Input: 15
    Output: 22
"""
def ans(r):
    total_chocolate = r
    empty_packet = r

    while empty_packet > 3:
        total_chocolate += empty_packet // 3
        empty_packet = empty_packet // 3 +  empty_packet % 3
    return total_chocolate

r = int(input())
print(ans(r))