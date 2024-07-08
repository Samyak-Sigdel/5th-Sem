
rows = int(input("Enter the number of rows for the half pyramid: "))
for i in range(1, rows + 1):
    print('*' * i)



n = 5
for i in range(1, n + 1):
    print(' ' * (n - i) + '*' * i)