a=int(input("enter a number"))
b=0
sum=0
c=a

if(a>9):
    while(a>0):
     b=a%10
     sum=sum+(b*b)
     a= a//10
elif(a>99):
    while(a>0):
     b=a%10
    sum=sum+(b*b*b)
    a= a//10
elif(a>999):
    while(a>0):
     b=a%10
    sum=sum+(b*b*b*b)
    a= a//10
elif(a>9999):
    while (a > 0):
        b = a % 10
    sum = sum + (b * b * b * b*b)
    a = a // 10
elif(a>99999):
    while (a > 0):
        b = a % 10
    sum = sum + (b * b * b * b*b*b)
    a = a // 10
else:
    print("your number is too big please anter a valid number")

if(sum==c):
    print ("your number is armstrong")
else:
    print("your number is not armstrong")