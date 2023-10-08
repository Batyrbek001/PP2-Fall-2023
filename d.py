a = list(map(int, input().split(" ")))
b = []

for i in a:
    if i in b:
        print("YES")
    elif i not in b:
        print("NO")
        b.append(i)
