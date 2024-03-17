#  Problem: Check ith bit is set or not.
# Problem Link: https://www.codingninjas.com/studio/problems/check-whether-k-th-bit-is-set-or-not_5026446?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf

# besic method.
a , i  = map(int, input().split())
binary_number = str(bin(a))
if(binary_number[len(binary_number)-1 - i] == "0"):
    print("Not Set")
else:
    print("Set")


# Best Approch
a , i  = map(int, input().split())
test = a ^ (1<<i)
if test == 0:
    print("Set")
else:
    print("Not set")