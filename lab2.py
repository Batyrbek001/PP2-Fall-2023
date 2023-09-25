1_________________________________________
n = int(input())
m = int(input())

print(min(n,m))


2_________________________________________
n = int(input())

if n > 0:
    print(1)

elif n < 0:
    print(-1)
    
else:
    print(0)


3_________________________________________
a = int(input())
b = int(input())
c = int(input())
d = int(input())

if (a%2==1 and b%2==1) and (c%2==1 and d%2==1):
    print("YES")
    
if (a%2==1 and b%2==1) and (c%2==0 and d%2==0):
    print("YES")
    
if (a%2==0 and b%2==0) and (c%2==0 and d%2==0):
    print("YES")
    
if (a%2==0 and b%2==0) and (c%2==1 and d%2==1):
    print("YES")
    
if (a%2==1 and b%2==0) and (c%2==1 and d%2==0):
    print("YES")
    
if (a%2==1 and b%2==0) and (c%2==0 and d%2==1):
    print("YES")
    
if (a%2==0 and b%2==1) and (c%2==0 and d%2==1):
    print("YES")
    
if (a%2==0 and b%2==1) and (c%2==1 and d%2==0):
    print("YES")
    

if (a%2==1 and b%2==1) and (c%2==0 and d%2==1):
    print("NO")

if (a%2==1 and b%2==1) and (c%2==1 and d%2==0):
    print("NO")
    
if (a%2==0 and b%2==0) and (c%2==0 and d%2==1):
    print("NO")
    
if (a%2==0 and b%2==0) and (c%2==1 and d%2==0):
    print("NO")
    
if (a%2==1 and b%2==0) and (c%2==1 and d%2==1):
    print("NO")
    
if (a%2==1 and b%2==0) and (c%2==0 and d%2==0):
    print("NO")
    
if (a%2==0 and b%2==1) and (c%2==1 and d%2==1):
    print("NO")
    
if (a%2==0 and b%2==1) and (c%2==0 and d%2==0):
    print("NO")


4_________________________________________
n = int(input())

if ((n%4==0) and (n%100!=0)) or (n%400==0):
    print ("YES")
    
else:
    print("NO")


5_________________________________________
a = int(input())
b = int(input())
c = int(input())

print(min(a,b,c))


6_________________________________________
a = int(input())
b = int(input())
c = int(input())

if a==b and a==c and b==c:
    print(3)
    
elif a==b or a==c or b==c:
    print(2)
    
else:
    print(0)


7_________________________________________
a = int(input())
b = int(input())
c = int(input())
d = int(input())

if a == c:
    print ("YES")
    
elif b==d:
    print ("YES")
    
else:
    print ("NO")


8_________________________________________
a = int(input())
b = int(input())
c = int(input())
d = int(input())

if ((c-a==1) or (c-a==0)) and ((d-b==1) or (d-b==0) or (b-d==1)):
    print ("YES")
    
elif ((a-c==1) or (a-c==0)) and ((b-d==1) or (b-d==0) or (d-b==1)):
    print ("YES")
    
else:
    print ("NO")


9_________________________________________
a = int(input())
b = int(input())
c = int(input())
d = int(input())

if abs(a - c) == abs(b - d):
    print('YES')
else:
    print('NO')


10_________________________________________
a = int(input())
b = int(input())
c = int(input())
d = int(input())

if ((a == c) or (b==d)) or (abs(a - c) == abs(b - d)):
    print('YES')
else:
    print('NO')


11_________________________________________
a = int(input())
b = int(input())
c = int(input())
d = int(input())

dx=abs(a-c)
dy=abs(b-d)

if dx==1 and dy==2 or dx==2 and dy==1:
    print("YES")
    
else:
    print("NO")


12_________________________________________
a = int(input())
b = int(input())
c = int(input())
d = int(input())

dx=abs(a-c)
dy=abs(b-d)

if dx==1 and dy==2 or dx==2 and dy==1:
    print("YES")
    
else:
    print("NO")


13_________________________________________
n = int(input())
m = int(input())
k = int(input())

if (k%m==0 or k%n==0) and (k<m*n):
    print("YES")
else:
    print("NO")


14_________________________________________
N = int(input())
M = int(input())
x = int(input())
y = int(input())

if M<N:
    if M-x<x:
        x=M-x
    if N-y<y:
        y=N-y
    
else:
    if N-x<x:
        x=N-x
    if M-y<y:
        y=M-y
        
if x<y:
    print(x)
    
else:
    print(y)
