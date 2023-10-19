a, b = map(int, input().split())
anya = set()
borya = set()

for i in range(a):
    anya.add(int(input()))
for i in range(b):
    borya.add(int(input()))

print(len(set(anya) & set(borya)))
print(*sorted(set(anya) & set(borya)))
print(len(set(anya) - set(borya)))
print(*sorted(set(anya) - set(borya)))
print(len(set(borya) - set(anya)))
print(*sorted(set(borya) - set(anya)))
