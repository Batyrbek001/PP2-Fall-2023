numbers = input()
numbers_list = [float(num) for num in numbers.split()]
 
result = 1
for num in numbers_list:
    result *= num
 
print(result)