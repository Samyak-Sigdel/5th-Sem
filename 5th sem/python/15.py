n = int(input("Enter the size of the array: "))
names = []
for i in range(n):
    name = input("Enter name {}: ".format(i + 1))
names.append(name)
names.sort()
print("Names in alphabetical order:")
for name in names:
    print(name)