"""
# Problem Stetment:
Given a string check for balanced parenthasis if it is balanced then 
return string as it is otherwise balance it.

i/p - {{{}
o/p - {{{}}}

i/p - }{{}}{
o/p - {}{{}}{}

i/p - }}}
o/p - {{{}}}

i/p - {}}{{}
o/p - {{}}{{}}
"""

def ans(s):
    stack = []
    for i in s:
        if i in '[{(':
            stack.append(i)
        else:
            if not stack:
                stack.append(i)
            elif(i == ')' and stack[-1] == '('):
                stack.pop()
            elif(i == '}' and stack[-1] == '{'):
                stack.pop()
            elif(i == ']' and stack[-1] == '['):
                stack.pop()
            else:
                stack.append(i)
    
    while stack:
        if stack[-1] == '(':
            s = s + ')'
        elif(stack[-1] == '['):
            s = s + ']'
        elif(stack[-1] == '{'):
            s = s + '}'
        elif(stack[-1] == '}'):
            s = '{' + s
        elif(stack[-1] == ']'):
            s = '[' + s
        elif(stack[-1] == ')'):
            s = '(' + s
        stack.pop()
    return s
            

s = input()
print(ans(s))