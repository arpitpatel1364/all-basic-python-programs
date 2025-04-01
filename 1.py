a = ["arpit", "dax", "smit", "pransh", "deep"]

while len(a) < 10:
    try:
        name = input("Enter name: ")
        if name not in a:
            a.append(name)
        else:
            print("Name was already in the list.")

    except :
        print("An error:")

print(a)