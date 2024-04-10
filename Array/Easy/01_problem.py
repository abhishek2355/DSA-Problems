# Problem Statement: Given an array, we have to find the largest element in the array.
def ans(test):
    max_ = float('-inf')
    for i in test:
        if i > max_:
            max_ = i
    return max_

test = list(map(int, input().split()))
print(ans(test))