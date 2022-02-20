class Solution:
    def firstMissingPositive(self, A):
        N = len(A)
        # case 1 : 1 to N
        for i in range(N):
            if A[i] <= 0 or A[i] > N:
                A[i] = N + 100000
        # negate indices
        for i in range(N):
            idx = abs(A[i]) - 1

            if 0 <= idx < N and A[idx] > 0:
                A[idx] = - A[idx]

        for i in range(N):
            if A[i] > 0:
                return i + 1

        # when all numbers are present [1,N]
        return N + 1















