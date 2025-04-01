
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))


min_num = min(a, b, c)
max_num = max(a, b, c)

count = 0


if min_num < max_num:
    while min_num <= max_num:
        print(min_num)
        count += 1
        min_num += 1
else:
    while min_num >= max_num:
        print(min_num)
        count += 1
        min_num -= 1


print("Numbers printed:", count)
