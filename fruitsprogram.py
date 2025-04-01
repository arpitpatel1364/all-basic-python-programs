name=input("enter the fruit name")
price=int(input(f"enter price of {name}"))
budget = 200
if (price <= budget):
    print("Alexa, add",name, "to the cart.")
else:
    print("sorry i don't want to buy")

