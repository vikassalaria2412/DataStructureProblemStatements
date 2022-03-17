"""
Given an integer array nums, handle multiple queries of the following type:

Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
"""


class NumArray:

    def __init__(self, nums: List[int]):
        self.presum = [nums[0]]
        for x in nums[1:]:
            self.presum.append(x + self.presum[-1])

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.presum[right]
        else:
            if left <= right:
                return self.presum[right] - self.presum[left - 1]

            else:
                return self.presum[right]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)