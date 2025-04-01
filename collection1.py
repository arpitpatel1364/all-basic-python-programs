A = []


while len(A) < 10:
    name = input("Enter your name: ")


    if name in A:
        print("Already exists. Please enter a different name.")
    else:
        A.append(name)

print(A)