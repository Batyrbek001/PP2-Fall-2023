def even_numbers(n):
    return (str(x) for x in range(0, n + 1,2))

n = int(input())
rez = even_numbers(n)

rez_str = ', '.join(rez)
print(rez_str)