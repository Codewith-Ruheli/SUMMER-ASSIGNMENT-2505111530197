#subract matrices
# First matrix
A = [[7, 8, 9],
     [4, 5, 6]]

# Second matrix
B = [[1, 2, 3],
     [1, 2, 3]]

# Result matrix
result = [[0, 0, 0],
          [0, 0, 0]]

# Subtracting matrices
for i in range(len(A)):
    for j in range(len(A[0])):
        result[i][j] = A[i][j] - B[i][j]

# Print result
print("Difference of matrices:")
for row in result:
    print(row)