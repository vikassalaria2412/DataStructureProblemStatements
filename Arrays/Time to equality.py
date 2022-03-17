
"""
Given an integer array A of size N. In one second you can increase the value of one element by 1.

Find the minimum time in seconds to make all elements of the array equal.
Input Format

First argument is an integer array A.


Output Format

Return an integer denoting the minimum time to make all elements equal.
"""
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        N = len(A)
        sortArray = sorted(A)
        count = 0
        for i in range(N - 2, -1, -1):
            value = sortArray[-1] - sortArray[i]
            count += value
        return count


A = [731, 349, 490, 781, 271, 405, 811, 181, 102, 126, 866, 16, 622, 492, 194, 735]
obj = Solution()
print(obj.solve(A))
######################
#Better Solution
import math


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        N = len(A)
        max = -(math.inf)
        count = 0
        for i in range(N):
            if A[i] > max:
                max = A[i]
        for i in range(N):
            temp = max - A[i]
            count += temp

        return count


