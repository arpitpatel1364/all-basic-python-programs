a=int(input("enter the first number"))
b=int(input("enter the second number"))
c=int(input("enter the third number"))

count = 0

if a==b==c:
    print("all numbers are equal")
    count+=1

if(a<b):
    for i in range(a,b):
        print(i)
        count+=1


else:
     for i in range(a,b,-1):
        print(i)
        count +=1

if(b<c):
    for i in range(b, c+1):
        print(i)
        count +=1


else:
    for i in range(b, c-1 , -1):
        print(i)
        count +=1

print("your number count is ",count)
