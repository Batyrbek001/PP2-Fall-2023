def Reverse(input_string):
    words = input_string.split()
    reverse = ' '.join(reversed(words))
    return reverse

user_input = input()
rez = Reverse(user_input)
print(rez)