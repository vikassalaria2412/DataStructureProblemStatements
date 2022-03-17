"""
You are given an array A of integers of size N.

Your task is to find the equilibrium index of the given array

Equilibrium index of an array is an index such that the sum of elements at
lower indexes is equal to the sum of elements at higher indexes.
"""


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        total = 0
        for x in A:
            total += x
        left = 0
        for i in range(n):
            right = total - left - A[i]
            if left == right:
                return (i)

            left += A[i]

        return -1









A = [ 1, 2, 3, 7, 1, 2, 3 ]

print(solve(A))