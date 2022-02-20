# """
# You are given an array of N integers, A1, A2, …. AN.
#
# Return the maximum value of f(i, j) for all 1 ≤ i, j ≤ N.
#  f(i, j) is defined as |A[i] - A[j]| + |i - j|, where |x| denotes absolute value of x.
# """
# # Pseudo code
# import sys
#
# """
# # Array with length N
# # for loop till length of Array
# # for loop till length of 1 to length of array + 1
# # find value = |A[i] - A[j]| + |i - j|
# # max = |A[i] - A[j]| + |i - j|
# # compare max greater than otherwise change max
#
# """
# # computatuonal bad approach
# # def absvalue(A):
# #     max = 0
# #     for i in range(len(A)):
# #         for j in range(i + 1,len(A)):
# #             value = abs(A[i] - A[j]) + abs(i - j)
# #             if max < value:
# #                 max = value
# #
# #     return max
# #
# # #A = [1, 3, -1]
# # #A = [2]
# # A = [ -70, -64, -6, -56, 64, 61, -57, 16, 48, -98 ]
# #
# # print(absvalue(A))
#
#
# def maxArray(A):
#     temp1 = 0
#     temp2 = 0
#     max1 = - sys.maxsize()
#     max2 = -sys.maxsize()
#     min1 = sys.maxsize()
#     min2 = sys.maxsize()
#     for i in range(len(A)):
#         temp1 =A[i] + i
#         temp2 = A[i] - i
#         max_value_1 = max
#         max1 = max(max1,temp1)
#         max2 = max(max2, temp2)
#         min1 = max(min1,temp1)
#         min2 = max(min2,temp2)
#     return max((max1 - min1 ),(max2 - min2))


import math


class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArr(self, A):
        temp1 = 0
        temp2 = 0
        max1 = -math.inf
        max2 = -math.inf
        min1 = math.inf
        min2 = math.inf
        for i in range(len(A)):
            temp1 = A[i] + i
            temp2 = A[i] - i

            max1 = max(max1, temp1)
            max2 = max(max2, temp2)
            min1 = min(min1, temp1)
            min2 = min(min2, temp2)
        return max((max1 - min1), (max2 - min2))

