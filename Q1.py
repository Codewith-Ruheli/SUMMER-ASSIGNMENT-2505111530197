#find missing number in array
arr = [1, 2, 3, 5]

n = 5

total = n * (n + 1) // 2
missing = total - sum(arr)

print("Missing number is:", missing)