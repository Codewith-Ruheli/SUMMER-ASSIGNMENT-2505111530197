#find column wise sum
A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

for j in range(len(A[0])):
    col_sum = 0
    for i in range(len(A)):
        col_sum += A[i][j]
    print("Sum of column", j + 1, "=", col_sum)