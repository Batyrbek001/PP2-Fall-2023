def squares(a, b):
    for n in range(a, b + 1):
        yield n**2

a = int(input())
b = int(input())

for square in squares(a, b):
    print(square)
