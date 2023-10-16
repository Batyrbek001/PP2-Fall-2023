def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    return False
    
number = input()
numbers = list(map(int, number.split()))
rez = has_33(numbers)
print(rez)