#remove duplicates from array
arr = [1, 2, 2, 3, 4, 4, 5]

new_arr = []

for i in arr:
    if i not in new_arr:
        new_arr.append(i)

print("Array after removing duplicates:", new_arr)