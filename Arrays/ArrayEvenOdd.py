"""
Count ways to make sum of odd and even indexed elements equal by removing an array element
##############################
Given an array, arr[] of size N, the task is to find the count of array
indices such that removing an element
from these indices makes the sum of
even-indexed and odd-indexed array elements equal.
"""

A=[2, 1, 6, 4]
#A=[1, 1, 1]

def eveOdd(A):
    N = len(A)
    temp = []
    count = 0
    for x in A:
        A.remove(x)
        even = 0
        odd = 0

        for y in range(len(A)):
            if y % 2 == 0:
                even += A[y]

            else:
                odd += A[y]

        if even == odd:
            count += 1









print(eveOdd(A))