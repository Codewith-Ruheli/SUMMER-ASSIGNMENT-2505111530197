#calculate sum of first N natural number
n = int(input("Enter N: "))

sum = 0
for i in range(1, n + 1):
    sum += i

print("Sum =", sum)
