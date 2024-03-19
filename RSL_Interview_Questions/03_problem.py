# Count occurrence of alphabets in a given string. let "aaabbbsssw" --> "a3b3s3w1"
from collections import Counter

def solution(s):
    if not s:
        return ""
    else:
        ans = ''
        current_char = s[0]
        char_count = 1
        for i in range(1, len(s)):
            if s[i] == current_char:
                char_count += 1
            else:
                ans += current_char + str(char_count)
                current_char = s[i]
                char_count = 1
        ans += current_char + str(char_count)
        return ans

# Count occurrence of alphabets in a given sentence
def answer(s):
    count = {}
    temp = set(s)
    for i in temp:
        if(i.isalpha()):
            count[i] = 0
    for i in s:
        if(i.isalpha()):
            count[i] += 1
    return count


s1 = input()
print(solution(s1))

s2 = input()
print(answer(s2))
