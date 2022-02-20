class Solution:
    def solve(self, A, B):
        if B % 4 == 0 :
            if A == 2:
                return 29
        if  B % 100 == 0 or B % 400 == 0:
        if A in {1, 3, 5, 7, 8, 10, 12}:
            return 31
        if A in {2, 4, 6, 9, 11}:
            return 30
        if B % 4 != 0 and A == 2:
            return 28
A = 2
B = 9100
obj = Solution()
obj.solve(A, B)










