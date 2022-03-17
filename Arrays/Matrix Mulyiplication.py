def solve( A, B):
    n = len(A)
    m = len(A[0])
    C = A[:][:]
    for i in range(n):
        for j in range(m):
            A[i][j] = A[i][j] * B[j][i]

        C.append(A[i][j])

   return  C

A =  [[1, 2],[3, 4]]
B = [[5, 6], [7, 8]]
print(solve(A,B))