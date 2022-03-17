# def rotationGame(A, B):
#     N = len(A)
#    # B = int(input())
#     for t in range(B):
#         for i in range(N - 1):
#             A[i],A[i + 1] = A[i + 1], A[i]
#     print(A)
#
# A = [ 1, 2, 3, 4, 5 ]
# B = 3
#
# 3 4 5 1 2
# print(rotationGame(A, B))

# d

def rotateA(A,B ):
    B = B % len(A)
    l, r = 0 , len(A) - 1
    while l < r:
        A[l], A[r] = A[r] , A[l]
        l, r = l + 1 , r - 1

    return A






A = [1,2,3,4,5,6,7,8]
B = 2
print(rotateA(A,B))