import math
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        max = - math.inf
        min = - math.inf
        for i in range(len(A)):
            if A[i] % 2 == 0:
                if A[i] > max:
                    max = A[i]
            else:
                if A[i] > min:
                    min = A[i]

        return (max - min)

A = [-98, 54, -52, 15, 23, -97, 12, -64,52, 85]
obj = Solution()
obj.solve(A)