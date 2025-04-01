a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("enter third number:"))
count=0
if a==b==c:
    count=1

if(a<b):
    while(a<b):
        print(a)
        count+=1
        a+=1
else:
    while(a>b):
        print(a)
        count += 1
        a-=1

if(b<c):
    while(b<=c):
        print(b)
        count += 1
        b+=1
else:
    while (b > c):
        print(b)
        count += 1
        b -= 1


print("the numbers are ",count)

