# Reverse String

def sol_1(s): #O(n)
    return s[::-1]

def sol_2(s): # O(n)
    ans = ''
    for i in s:
        ans  = i + ans
    return ans

def sol_3(st):
    s = list(st)
    print(s)
    start = 0
    end  = len(s)-1

    while start < end:
        temp = s[start]
        s[start] = s[end]
        s[end] = temp
        start += 1
        end -= 1
    return s.join("")


s = input()
print(sol_1(s))
print(sol_2(s))
print(sol_3(s))