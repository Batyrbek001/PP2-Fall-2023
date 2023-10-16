def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    return False
    
number = input()
numbers = list(map(int, number.split()))
rez = has_33(numbers)
print(rez)

def Palindrome(s):
    return s == s[::-1]

text = input()
if Palindrome(text):
    print('Yes')
else:
    print('No')

def histogram(numbers):
    for num in numbers:
        print('*' * num)

num_str = input()
nums = [int(item) for item in num_str.split()]
histogram(nums)