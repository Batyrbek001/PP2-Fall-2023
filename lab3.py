1)
n = input().split(" ")

for i in range(len(n)):
    if(i%2==0):
        print(n[i], end=" ")
______________________________________________________

2)
n = list(map(int, input().split(" ")))

for i in range(len(n)):
    if n[i]%2==0:
        print(n[i], end=" ")
______________________________________________________

3)
n = list(map(int, input().split(" ")))

for i in range(1, len(n)):
    if n[i]>n[i-1]:
        print(n[i], end = " ")
______________________________________________________

4)
s = list(map(int, input().split(" ")))

for i in range(len(s)-1):
    if (s[i]>0 and s[i+1]>0) or (s[i]<0 and s[i+1]<0):
        print(s[i], s[i+1],end = ' ')
        break
______________________________________________________

5)
s = list(map(int, input().split(" ")))
res = 0
for i in range(1, len(s) - 1):
    if s[i] > s[i-1] and s[i] > s[i+1]:
            res+=1
print(res)
______________________________________________________

6)
n = list(map(int, input().split(" ")))

index = 0
max = n[0]

for i in range(1, len(n)):
    if n[i]>max:
        index=i
        max=n[i]
print(max, index)
______________________________________________________

7)
n = list(map(int, input().split(" ")))
m = int(input())
sum = 1;

for i in range(len(n)):
    if m <= n[i]:
        sum+=1
print(sum)
_______________________________________________________

8)
n = list(map(int, input().split(" ")))
res=1

for i in range(len(n)-1):
    if n[i]!=n[i+1]:
        res+=1
print(res)
_______________________________________________________

9)
n = list(map(int, input().split(" ")))

for i in range(0, len(n)-1,2):
    n[i], n[i+1] = n[i+1], n[i]
print(" ".join(str(i)for i in n))
_______________________________________________________

10)
n = list(map(int, input().split(" ")))

index_max=0
index_min=0

for i in range(1, len(n)):
    if n[i]>n[index_max]:
        index_max=i
    if n[i]<n[index_min]:
        index_min=i
n[index_max], n[index_min] = n[index_min], n[index_max]
print(" ".join(str(i)for i in n))
_______________________________________________________

11)
n = list(map(int, input().split(" ")))
m = int(input())

for i in range(len(n)):
    if m==i:
        continue
    print(n[i], end= " ")
_______________________________________________________

12)
n = list(map(int, input().split(" ")))
x, y = list(map(int, input().split(" ")))
n.insert(x,y)
print(" ".join(str(i)for i in n))
_______________________________________________________

13)
n = list(map(int, input().split(" ")))
res = 0

for i in range(len(n)):
    for j in range(i+1, len(n)):
        if n[i]==n[j]:
            res+=1
print(res)
_______________________________________________________

14)
n = list(map(int, input().split(" ")))
m=[]

for i in range(len(n)):
    if n.count(n[i])==1:
        print(n[i], end=" ")
_______________________________________________________

15)
N, K = list(map(int, input().split(" ")))
x = ['I'] * N

for j in range(K):
    l,r = list(map(int, input().split(" ")))
    x[l-1:r] = ['.'] * (r-l+1)
print("".join([str(i)for i in x]))
_______________________________________________________

16)
n = 8
x = [0] * n
y = [0] * n
result = 'NO'
for i in range(n):
    x[i], y[i] = list(map(int, input().split(" ")))
for i in range (n):
    for j in range(i+1,n):
        if x[i]==x[j] or y[i]==y[j] or abs(x[i]-x[j])==abs(y[i]-y[j]):
            result = 'YES'
print(result)
