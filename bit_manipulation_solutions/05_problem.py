# Problem Link: https://leetcode.com/problems/subsets/description/


# Iterative
def subset(nums):
    ans = []
    temp = []
    ans.append(temp)
    for i in nums:
        n = len(ans)
        for j in range(0,n):
            temp = ans[j].copy()
            temp.append(i)
            ans.append(temp)
    return ans

nums = [1, 2, 3]
print(subset(nums))

# recursive 
def generateSubSet(index,nums,test,ans):
        ans.append(test.copy())
        for i in range(index,len(nums)):
            test.append(nums[i])
            generateSubSet(i+1,nums,test,ans)
            test.pop(len(test)-1)

def subset(nums):
    ans = []
    test=[]
    generateSubSet(0,nums,test,ans)
    return ans

nums = [1, 2, 3]
print(subset(nums))

# Optimal 
def subset(nums):
    subset = 1 << len(nums)
    ans = []

    for i in range(subset):
        test = []
        for j in range(len(nums)):
            if(i & 1<<j != 0):
                test.append(nums[j])
        ans.append(test)
    return ans


nums = [1,2,3]
print(subset(nums))

        

        