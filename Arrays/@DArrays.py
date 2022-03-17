def solve(A):
    D = []
    for i in range(len(A[0])):
        C = 0

        for j in range(len(A)):
            temp = A[j][i]
            C += temp

        D.append(C)

    return D
A =[[1,2,3,4],[5,6,7,8],[9,2,3,4]]
print(solve(A))