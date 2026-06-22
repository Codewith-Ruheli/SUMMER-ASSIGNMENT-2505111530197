#multiply matrices
# First matrix
A = [[1, 2],
     [3, 4]]

# Second matrix
B = [[5, 6],
     [7, 8]]

# Result matrix
result = [[0, 0],
          [0, 0]]

# Matrix multiplication
for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            result[i][j] += A[i][k] * B[k][j]

# Print result
print("Product of matrices:")
for row in result:
    print(row)