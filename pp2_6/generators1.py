def squares(N):
    for i in range(1, N+1):
        yield i**2

N = int(input())
rez = squares(N)

for square in rez:
    print(square)
