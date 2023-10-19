a = int(input())
b = ""
for i in range(a):
    b1 = input().replace('\n', ' ')
    b += ' ' + b1
res = b.strip().split(" ")
print(len(set(res)))
