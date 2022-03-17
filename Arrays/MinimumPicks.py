import math
# class Solution:
    # @param A : list of integers
    # @return an integer
def solve(A):
    maxEven = -(math.inf)
    minOdd = (math.inf)
    for i in range(len(A)):
        if A[i] % 2 == 0:
            if A[i] > maxEven:
                maxEven = A[i]

        else:
            if A[i] < minOdd:
                minOdd = A[i]


    diff = maxEven - minOdd

    return diff

A = [ -98, 54, -52, 15, 23, -97, 12, -64, 52, 85 ]

print(solve(A))