A = [[1,2,3],[4,5,6],[7,8,9]]
B = [[11,12,13],[14,15,16],[17,18,19]]
def traverse(A,B):
    n = len(A)
    m = len(A[0])
    c = A[:] [:]
    for i in range(n):
        for j in range(m):
            c[i][j] = A[i][j] + B[i][j]


    return c



    # for i in range(len(c)):
    #     for j in range(len(c[0])):
    #         print(c[i][j], end = " ")

       # print()







print(traverse(A,B))
#print(A)