# Swap 2 number a = 10, b = 20 After swap a = 20, b = 10

# 1. besic method.
a, b  = map(int, input().split())
print("Before Swap ", a, b)
temp  = a
a = b
b = temp
print("After swap",a, b)

# 2. Using XOR : we know that XOR of same number is 0.
a, b  = map(int, input().split())
print("Before Swap ", a, b)
a = a ^ b
b = a ^ b  # (a ^ b) ^ b --> a
a = a ^ b  # (a ^ b) ^ a
print("After swap",a, b)

