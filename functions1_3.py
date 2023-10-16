def solve(numheads, numlegs):
    for num_chickens in range(numheads + 1):
        num_rabbits = numheads - num_chickens
        if (2 * num_chickens + 4 * num_rabbits) == numlegs:
            return num_chickens, num_rabbits
    return None, None 

numheads = int(input())
numlegs = int(input())

chickens, rabbits = solve(numheads, numlegs)

if chickens is not None:
    print(chickens)
    print(rabbits)
else:
    print()
