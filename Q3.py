#transpose matrix
# Original matrix
A = [[1, 2, 3],
     [4, 5, 6]]

# Transpose matrix
transpose = [[0, 0],
             [0, 0],
             [0, 0]]

for i in range(len(A)):
    for j in range(len(A[0])):
        transpose[j][i] = A[i][j]

print("Transpose of matrix:")
for row in transpose:
    print(row)