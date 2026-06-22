#Wap to add matrices
# First matrix
A = [[1, 2, 3],
     [4, 5, 6]]

# Second matrix
B = [[7, 8, 9],
     [1, 2, 3]]

# Result matrix
result = [[0, 0, 0],
          [0, 0, 0]]

# Adding matrices
for i in range(len(A)):
    for j in range(len(A[0])):
        result[i][j] = A[i][j] + B[i][j]

# Print result
print("Sum of matrices:")
for row in result:
    print(row)