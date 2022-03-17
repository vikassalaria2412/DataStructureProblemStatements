"""
Given an array A, find the size of the smallest subarray such that it
 contains at least one occurrence of the maximum value of the array

and at least one occurrence of the minimum value of the array.
"""


import math


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        maxval = -(math.inf)
        minval = (math.inf)
        for i in range(n):
            if A[i] > maxval:
                maxval = A[i]

            if A[i] < minval:
                minval = A[i]

        imax = -1
        imin = -1
        ans = math.inf
        for i in range(n):
            if A[i] == minval:
                imin = i

            if A[i] == maxval:
                imax = i
            if imax != -1 and imin != -1:
                ans = min(ans, abs(imin - imax) + 1)

        return ans


