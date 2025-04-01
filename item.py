item=input("enter that item name")
x=int(input("enter your item price here"))
if x < 0:
    print("please enter a valid price")
elif x>10000:
    print("this is a 1930's whisky you choosing an amazing item")
elif x >8500:
    print("this is a 1945's whisky that was so good ")
elif x > 6000:
    print(" this is an 1960's your choosing item was good")
elif x > 4000:
    print(" this is an 1970's whisky you choosing good item ")
elif x > 2500:
    print(" this is an 1985's whisky you choosing  item was not bad")
elif x > 1000:
    print(" this is an 1999's whisky you choosing item was average ")
elif x > 850:
    print("  this is an after 2000's whisky you need to go for other one  ")
else:
    print(" visit again")