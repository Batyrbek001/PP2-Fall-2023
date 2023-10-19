def Centigrade(F):
    C = (5 / 9) * (F - 32)
    return C

F = int(input())
rez = Centigrade(F)
print(rez)