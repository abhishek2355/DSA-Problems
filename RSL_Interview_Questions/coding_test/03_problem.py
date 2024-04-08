"""
# Problem Stetment:
Write a function that takes an input parameter as a String. The function should replace the alternate
words in it with “xyz” and print it. Words are separated by dots. (Avoid using inbuilt functions)

# Test Case:
If input is “i.like.this.program.very.much”
Output will be “i.xyz.this.xyz.very.xyz”
"""

# Sol. 1:
def replace_str(s):
    ans = ""
    flag = False
    count = 0

    for i in s:
        if i == ".":
            count += 1
            if(count % 2 != 0):
                flag = True
        elif(count % 2 == 0):
            ans += i
        elif(flag):
            ans += "XYZ"
            flag = False
    return ans

# Sol. 2:
def using_split(s):
    test = s.split('.')
    for i in range(len(test)):
        if i % 2 != 0:
            test[i] = 'XYZ'
    return ''.join(test)

s = input("Enter the string: ")
print('Final answer: ', replace_str(s))
print('Final answer: ', using_split(s))
