n = int(input("Enter the size of the array: "))
arr = []
print("Enter the elements of the array separated by space:")
arr = list(map(int, input().split()))
min_val = min(arr)
max_val = max(arr)
print("Min =", min_val)
print("Max =", max_val)