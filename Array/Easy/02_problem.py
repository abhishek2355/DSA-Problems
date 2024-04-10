# Problem Statement: Given an array, find the second smallest and second largest element in the array. 
# Print ‘-1’ in the event that either of them doesn’t exist.

def secondMax(test):
    if len(test) != 0:
        first_max = test[0]
        second_max = float('-inf')

        for i in test:
            if i > first_max:
                second_max = first_max
                first_max = i
            elif i > second_max and i != first_max:
                second_max = i
        return second_max

def secondMin(test):
    if len(test) != 0:
        first_min = test[0]
        second_min = float('inf')

        for i in test:
            if i < first_min:
                second_min = first_min
                first_min = i
            elif i < second_min and i != first_min:
                second_min = i
        return second_min



test = list(map(int, input().split()))
print(secondMax(test))
print(secondMin(test))