# Problem Link: https://leetcode.com/problems/find-the-original-array-of-prefix-xor/description/

# With extra space.
def findArray(pref):
    ans = []
    n = len(pref)
    if n == 1:
        return pref
    else:
        ans.append(pref[0])
        for i in range(1, len(pref)):
            ans.append(pref[i] ^ pref[i-1])
        return ans

# Without using extra space.
def optimal(pref):
    ans = []
    n = len(pref)
    if n == 1:
        return pref
    else:
        for i in range(n -1, 0, -1):
            pref[i] =  pref[i] ^ pref[i-1]
        return pref
    

pref = [5,2,0,3,1]
print(findArray(pref))
print(optimal(pref))