"""
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The relative order of the elements may be changed.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
"""
from array import *
from array import array

arr = array('i',[0,1,2,2,3,0,4,2])
val = 2


)

###################
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        N = len(nums)
        next_num = 0
        count = 0
        for i in range(N):
            if nums[i] != val:
                nums[next_num] = nums[i]
                next_num += 1
                count += 1

        return count


    ##############
    # fastest
    class Solution:
        def removeElement(self, nums: List[int], val: int) -> int:
            A = nums
            if len(A) < 1:
                return len(A)
            L, R = 0, len(A) - 1
            c = 0
            while L <= R:
                if A[R] == val:
                    R -= 1
                    c += 1
                elif A[L] != val:
                    L += 1
                elif A[L] == val:
                    A[L], A[R] = A[R], A[L]
                    L += 1
                    R -= 1
                    c += 1
            return len(A) - c





