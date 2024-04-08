"""
# Problem Stetment:
Given an price in (rs) our task is to return How many 2's and 5's coins are needed to achive this price.

# Test Case:
    1. input: 30
       output: Number of 5's coins are: 6
    2. input: 31
       output: Number of 5's coins are: 5, number of 2's coins are 3
"""

def ans(n):
    if n < 5:
        if n % 2 == 0:
            print("Number of 2 coins: ", n // 2)
        else:
            print("Enter the valid price value.")
    else:
        if n % 5 == 0 :
            print("Number of 5 coins: ", n // 5)
        else:
            r  = n % 5
            number_5 = n // 5

            if r % 2 == 0:
                print("Number of 5 coins: ", number_5)
                print("Number of 2 coins: ", r // 2)
            else:
                number_5 -= 1
                total = number_5 * 5
                rem = n - total
                print("Number of 5 coins: ", number_5)
                print("Number of 2 coins: ", rem // 2)

n = int(input("Enter the price in (rs): "))
ans(n)
