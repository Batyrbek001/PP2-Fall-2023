def histogram(numbers):
    for num in numbers:
        print('*' * num)

num_str = input()
nums = [int(item) for item in num_str.split()]
histogram(nums)