#moves zero to end
arr = [1, 0, 2, 0, 3, 4, 0, 5]

result = []

for i in arr:
    if i != 0:
        result.append(i)

zero_count = arr.count(0)

for i in range(zero_count):
    result.append(0)

print("Array after moving zeroes:", result)