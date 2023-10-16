from itertools import permutations

def Permutations(input_string):
    perms = permutations(input_string)

    for perm in perms:
        print("".join(perm))

user_input = input()
print()
Permutations(user_input)
