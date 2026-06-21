#find pair with given sum
arr = [2, 4, 7, 11, 15]
target = 9

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] + arr[j] == target:
            print("Pair found:", arr[i], arr[j])