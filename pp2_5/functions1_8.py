def spy_game(nums):
    count = 0 

    for num in nums:
        if num == 0:
            count += 1
        elif count >= 2 and num == 7:
            return True

    return False

number = input()
numbers = list(map(int, number.split()))
rez = spy_game(numbers)
print(rez)