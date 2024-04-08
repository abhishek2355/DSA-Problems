# Problem Statement: Given a circular integer array A, return the next greater element for every element in A. 
# The next greater element for an element x is the first element greater than x that we come across while traversing 
# the array in a clockwise manner. If it doesn’t exist, return -1 for this element.

def answer(arr):
    stack = []
    ans = []

    for i in range(len(arr)-1, -1, -1):
        
        if(len(stack) > 0):
            while len(stack) > 0 and arr[i] > stack[-1]:
                stack.pop(len(stack)-1)
            ans.append(stack[-1])
            stack.append(arr[i])
            print(stack)
        else:
            stack.append(arr[i])
            print(stack)
    return ans



arr = [3,10,4,2,1,2,6,1,7,2,9]
print(answer(arr))