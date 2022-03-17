def sortedArrays(A):
    N = len(A)
    next_num = 0

    for i in range(N):
        if i == 0 or A[i] != A[i - 1]:
            A[next_num] = A[i]
            next_num += 1



    return (next_num, A)








A = [0,0,0,0,1,1,1,1,2,2,2,2,3,3,3,5,5,5]
print(sortedArrays(A))

