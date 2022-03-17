def solve(A):
    m = len(A)
    n = len(A[0])
    C = []
    for i in range(m):
        C.append([0] * n)

    for i in range(m):
        for j in range(m):
            C[i][j] = A[j][i]

    return C

A = [[1, 2],[4, 5],[7, 8]]

print(solve(A))
