def Palindrome(s):
    return s == s[::-1]

text = input()
if Palindrome(text):
    print('Yes')
else:
    print('No')