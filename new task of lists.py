a = []
b = []
c = []

while len(a) < 5 or len(b) < 5 or len(c) < 5:
    value = int(input("Enter a number: "))

    if len(a) < 5 and value not in a:
        a.append(value)
        print(a, b, c)
    elif len(b) < 5 and value not in b:
        b.append(value)
        print(a, b, c)
    elif len(c) < 5 and value not in c:
         c.append(value)
         print(a, b, c)
    else:
        print("Your number is already in all lists or the list is full.")

a.append(b)
a.append(c)
print(a)  