# Input values
x = int(input())  # Length of cuboid along x-axis
y = int(input())  # Length of cuboid along y-axis
z = int(input())  # Length of cuboid along z-axis
n = int(input())  # Given sum that should be excluded

# Using list comprehension to generate all valid coordinates
coordinates = [[i, j, k] for i in range(x) for j in range(y) for k in range(z) if i + j + k != n]

# Printing the result
print(coordinates)
