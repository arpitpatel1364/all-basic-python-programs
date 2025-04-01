a=21
b=22

if a%2==0 and a!=0:
    if b%2==0 and b!=0:
        print("a is even b is even")

    elif b%2!=0:
        print("a is even b is odd")

    else:
        print("a is even b is zero")
elif a%2!=0:
    if b % 2 == 0 and b!=0:
        print("a is odd b is even")

    elif b % 2 != 0:
        print("a is odd b is odd")

    else:
        print("a is odd b is zero")
else:
    if b % 2 == 0 and b!=0:
        print("a is zero b is even")

    elif b % 2 != 0:
        print("a is zero b is odd")

    else:
        print("a is zero b is zero")

