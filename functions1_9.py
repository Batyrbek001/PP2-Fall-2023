import math

def Volume(r):
    V = (4/3) * math.pi * r**3
    return V

r = int(input())
rez = Volume(r)
print(rez)