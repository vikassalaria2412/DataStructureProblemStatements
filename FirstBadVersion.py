class Solution:
    def firstBadVersion(self, n: int) -> int:
        start = 1
        end = n

        while (start < end):
            mid = (start + end) // 2
            if isBadVersion(mid):
                end = mid

            else:
                start = mid + 1

        return start

def isBadVersion(number):
    if number in (5,6,7,8,9,10,11,12,13):
        return True


    else:
        return False




obj = Solution()
obj.firstBadVersion(13)
