# # ineffective method
# # def factorial(A):
# #     answer = 1
# #     for i in range(A,1,-1):
# #         answer = answer * i
# #     print (answer)
# #
# #
# #
# # factorial(400000000000)
#
# # Dynamic programing
# def fact(N):
#     arr = {}
#     if N in arr:
#         return arr[N]
#     elif N == 0 or N == 1:
#         return 1
#         arr[N] = 1
#
#     else:
#         factorial = N * fact(N - 1)
#         arr [N ] = factorial
#     return factorial
#
# N = 15
# print(fact(N))

class Solution:

    # @param A : integer
    # @return an integer
    def solve(self, A):
        arr = {}
        def fact(B):

            if B in arr:
                return arr[B]

            elif B == 0 or B == 1:
                return 1
                arr[B] = 1

            else:
                factorial = B * fact(B - 1)
                arr[B] = factorial

            return factorial

        factorial = fact(A)
        return factorial




A = 5
obj = Solution()
print(obj.solve(A))

