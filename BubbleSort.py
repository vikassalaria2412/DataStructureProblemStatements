"""
Implement Bubble Sort in the article below.

Given an integer array A of size N, sort the array using bubble sort algorithm.
Return the array after sorting.
"""
# A = [2,7,3,6,44,21,32]
# A = [ 627, 619, 852, 472, 858, 994, 323, 738, 177, 625, 946, 730, 832, 12, 526, 361, 343, 782, 289 ]
A = [6,7,9,8]
def sortArray(A):
    for i in range(len(A)):
        for j in range(len(A) - 1):
            if A[j] > A[j + 1]:
                A[j] , A[j + 1] = A[j + 1], A[j]

    return A


print(sortArray(A))




