def twoSum( nums,target):
    A = sorted(nums)
    N = len(A)
    start = 0
    last = N
    mid = 0
    while (start <= last):
        mid = (start + last) // 2
        if A[mid] + A[mid + 1] < target:
            start = mid + 1

        elif (A[mid] + A[mid + 1]) == target:
            return (mid, mid + 1)


        else:
            last = mid - 1

nums = [3,2,4]
target = 6
print(twoSum(nums,target))