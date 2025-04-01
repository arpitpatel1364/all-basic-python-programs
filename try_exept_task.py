a=["arpit","dax","smit","pransh","deep"]
l=len(a)
while len(a) < 10:
 name=input("enter name")
 if name in a :
     print("name was alredy in list")
 else:
        a.append(name)

print(a)

