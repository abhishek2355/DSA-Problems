"""
# Problem Stetment: 
If given String is I_LOVE_INDIA reverse whole string 
except "_". Output for this would be A_IDNI_EVOLI
"""
def ans(input_string):
    s = list(input_string)
    i = 0
    j = len(s) -1

    while i < j:
        if s[i] == '_':
            i += 1
            continue
        
        if s[j] == '_':
            j -= 1
            continue

        temp = s[i]
        s[i] = s[j]
        s[j] = temp
        i += 1
        j -= 1
    return "".join(s)

s = input('Enter the string: ')
print(ans(s))