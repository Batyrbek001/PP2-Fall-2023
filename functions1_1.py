def Ounces(grams):
    ounces = 28.3495231 * grams
    return ounces

grams = int(input())
rez = Ounces(grams)
print(rez)