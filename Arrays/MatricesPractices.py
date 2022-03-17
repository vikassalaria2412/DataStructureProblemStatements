def matrices(A):
    n = len(A)
    m = len(A[0])
    C = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            v = (j + 1) ** (i + 1)
            C[i][j] = v

    return C

print(matrices(A))

