class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        start = 1
        end = A
        mid = 0
        while(start <= end):
            mid = (start + end) // 2
            if mid*mid == A:
                return mid
            elif mid * mid > A:
                end = mid - 1

            else:
                start = mid + 1

        return -1
