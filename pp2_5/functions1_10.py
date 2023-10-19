def Unique_elements(input_list):
    unique_list = []

    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)

    return unique_list

list_numbers = input()
numbers = [int(item) for item in list_numbers.split()]
unique_elements = Unique_elements(numbers)
print(unique_elements)