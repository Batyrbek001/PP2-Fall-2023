def palindrome(str):
    reverse_str = ''.join(str.split()).lower()
    return reverse_str == reverse_str[::-1]
    
s = input()

if palindrome(s):
    print("Yes")
else:
    print("No")