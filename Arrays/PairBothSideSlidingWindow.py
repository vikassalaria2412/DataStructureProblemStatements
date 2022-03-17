def pair(A, B):
    countsum = 0
    maxsum = 0
    for i in range(B):
        countsum += A[i]

    maxsum = countsum
    j = len(A) - 1
    for i in range(B - 1, -1 , -1):
        countsum = countsum +A[j] - A[i]
        maxsum = max(countsum, maxsum)
        j  -=  1


    return maxsum
A = [5,-2,3,1,2]
B = 3
print(pair(A,B))







