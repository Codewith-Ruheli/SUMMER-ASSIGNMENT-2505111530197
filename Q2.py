#check symmetric matrix
A = [[1, 2, 3],
     [2, 4, 5],
     [3, 5, 6]]

symmetric = True

for i in range(len(A)):
    for j in range(len(A)):
        if A[i][j] != A[j][i]:
            symmetric = False
            break

if symmetric:
    print("Matrix is Symmetric")
else:
    print("Matrix is Not Symmetric")
    