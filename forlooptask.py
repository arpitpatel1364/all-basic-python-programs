a=int(input("enter the first number"))
b=int(input("enter the second number"))


if a<b:
 for i in range(a,b+1):
  print(i)

else:
  for i in range(a,b-1,-1):
   print(i)